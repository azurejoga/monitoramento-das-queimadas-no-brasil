# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43faae46-f19c-362e-866a-26d31e492d0f | -21.6656 | -56.31764 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ada5df62-cac3-33fb-9da0-a3d9404d1a29 | -21.66527 | -56.32099 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e105457-e37c-3199-b536-602905b9f70c | -21.69307 | -56.30765 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 055e6a8b-ab40-3924-a2e7-66124dbd772f | -22.18784 | -56.96748 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2168ecfa-3447-3d1c-861a-ed595be77edf | -22.18867 | -56.96659 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e49bef9-da0d-3fbc-bea9-2d6a0a1936bc | -21.69831 | -56.30826 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10527ef5-4088-3b31-ae2d-a6dcf5f42775 | -16.42991 | -54.91661 | 2026-04-02 05:33:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73417572-06e1-3363-8df6-ab19d8d65046 | -16.43607 | -54.91031 | 2026-04-02 05:33:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85b56791-e1f3-324d-88d9-3cc37b16b5ad | -22.18833 | -56.96977 | 2026-04-02 05:33:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d40c62a-4342-3419-a8e4-3228f90bb56d | -21.70704 | -48.42393 | 2026-04-02 06:08:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 429e74d9-24f6-3084-b226-a3385e33a455 | -23.02806 | -52.68012 | 2026-04-02 12:08:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a6d2fad9-2758-32de-9185-86cabe14da7a | -18.93478 | -46.97919 | 2026-04-02 12:08:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 916e6277-fda4-3ec0-9ec2-96562aea7aba | -19.30634 | -49.69844 | 2026-04-02 12:08:00 | TERRA_M-T | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9941422a-c387-3515-b026-e914d75a6c39 | -21.29455 | -46.78451 | 2026-04-02 12:08:00 | TERRA_M-T | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| e7f53355-9330-30a1-b204-8928ad689559 | -21.6795 | -56.3142 | 2026-04-02 14:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 777512a7-ddf4-33cb-a56d-9709496bdade | -21.6795 | -56.3142 | 2026-04-02 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2064e1dc-1985-3572-b10a-8edb620116d2 | -21.659 | -56.3175 | 2026-04-02 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 224cee3a-e4fb-3136-9f05-0581d7e933ff | -21.659 | -56.3175 | 2026-04-02 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 3554ea30-0893-3d37-81b9-a02dc1ebcc45 | -21.6795 | -56.3142 | 2026-04-02 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b232fa42-9cbc-3d5e-af11-0459fff276b0 | -21.659 | -56.3175 | 2026-04-02 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 253da2a7-0881-3147-a60e-99a0154a7aca | -21.6795 | -56.3142 | 2026-04-02 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 93.0 |


