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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f802c870-da29-3435-8608-3bad2f7d6170 | -12.6595 | -44.4882 | 2025-08-02 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 554.1 |
| 0feb9c84-b4e2-3b2b-8cdd-a96fdc5a446f | -12.6789 | -44.4851 | 2025-08-02 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 35badca6-0da5-3d4a-8c4c-f27970c5529b | -12.6398 | -44.5148 | 2025-08-02 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 9238447a-d507-3ea3-9d6e-3549e0ea61f2 | -7.5595 | -44.7972 | 2025-08-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0b16ea23-9a7b-3198-bd64-86a6e205efd6 | -8.0324 | -43.1022 | 2025-08-02 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 264.5 |
| f7b1ba21-c8e5-33f8-b250-b02271adb066 | -11.5102 | -44.3401 | 2025-08-02 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d3329c02-ab2e-3dae-964b-55d5d5e3e6fc | -11.5102 | -44.3401 | 2025-08-02 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 4bcc3d37-c1d4-3b05-b780-377479dcaf87 | -8.0318 | -43.1493 | 2025-08-02 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 360.5 |
| e10cfe4f-7fd3-32fd-9918-ee9cf62c2773 | -14.1872 | -45.4406 | 2025-08-02 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| e73b913f-093b-333d-bf12-05265c04e467 | -12.6402 | -44.4913 | 2025-08-02 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 488.9 |
| c2bb68ea-ef98-30aa-95bc-25c82a3a5878 | -12.6398 | -44.5148 | 2025-08-02 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.3 |
| a711839d-b1dd-34b7-ae25-42f720e2648d | -3.4258 | -48.9663 | 2025-08-02 14:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cd53ed36-3dec-3f4c-bb46-962bfc565c0f | -14.1682 | -45.4208 | 2025-08-02 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| b7c89e09-8e90-32e4-ade1-1907141678f5 | -12.6789 | -44.4851 | 2025-08-02 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 303.6 |
| 73ff74ed-1ef1-3e71-bab6-7e5d5447224f | -11.5106 | -44.3167 | 2025-08-02 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 484bf345-b8b4-3e27-b6a8-142711ae6a1e | -12.6595 | -44.4882 | 2025-08-02 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 735.8 |
| 74994469-c1cd-342e-9add-e3fed4fbde42 | -6.7997 | -43.8312 | 2025-08-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 78cda44c-a3e7-3271-a8a3-3f5a903bd798 | -12.6586 | -44.5351 | 2025-08-02 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 247.7 |
| 53bcb86d-650d-3c08-8d11-423d373dd01b | -14.1872 | -45.4406 | 2025-08-02 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| bb6a19bc-82bb-3fc6-8b7d-b061dbb81a3e | -12.6398 | -44.5148 | 2025-08-02 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 251fa1c4-5215-3649-8c01-6ded3fdfcdfc | -11.5102 | -44.3401 | 2025-08-02 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4017d5fc-fe88-3e35-9e12-9f274e818691 | -6.7997 | -43.8312 | 2025-08-02 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| de6a8794-05ad-37a4-baa5-8aa149adc9ea | -5.564 | -43.607 | 2025-08-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 22b94230-d20a-381f-9c1d-d4a0b7e41426 | -12.6595 | -44.4882 | 2025-08-02 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 836.8 |
| aaf18d91-9760-3b0a-b04f-86735983aa9e | -12.6789 | -44.4851 | 2025-08-02 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 323.2 |
| 070669dd-17b3-30d5-9882-2aed27874265 | -9.1937 | -45.2886 | 2025-08-02 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 626ad7ff-175c-3a28-81bb-2ec2bf6831f1 | -12.6586 | -44.5351 | 2025-08-02 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 285.9 |


