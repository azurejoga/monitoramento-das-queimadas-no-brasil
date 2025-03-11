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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb832b41-1b69-371d-8684-c52baa4e97fd | -15.9482 | -48.11587 | 2025-03-11 05:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ed8cbe0-a0fb-3c73-9dab-f7ecfa0b22c3 | -10.40234 | -47.98124 | 2025-03-11 05:42:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4378dcb6-d90b-35e8-bde8-56a8bb7df822 | -5.20441 | -38.05838 | 2025-03-11 12:02:00 | TERRA_M-T | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0f458dff-9cae-30b2-b60d-23e4720c0590 | -8.89534 | -36.4143 | 2025-03-11 12:04:00 | TERRA_M-T | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 381d8f73-5db3-30db-92b4-2111d5fa5795 | -11.19866 | -38.95843 | 2025-03-11 12:04:00 | TERRA_M-T | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 14f099a8-8fc1-37e8-98ff-135dde6ec953 | -12.56229 | -39.62093 | 2025-03-11 12:04:00 | TERRA_M-T | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 2fb7149c-4fbb-397c-bdc3-3253fe364fef | -9.11509 | -37.57788 | 2025-03-11 12:04:00 | TERRA_M-T | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 51b615d2-2c25-35e6-ad6a-9291b8c0bef9 | -9.1165 | -37.56764 | 2025-03-11 12:04:00 | TERRA_M-T | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 4f2f2947-2d69-3861-94e1-ee0138af6a33 | -8.70952 | -36.96298 | 2025-03-11 12:04:00 | TERRA_M-T | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 23bcdf6b-7dc0-3c9f-ad62-0e6b5617ba13 | -16.33851 | -42.6521 | 2025-03-11 12:04:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1c29e9bc-1d05-3b6c-bb64-a723a6640b0c | -8.58117 | -36.24878 | 2025-03-11 12:04:00 | TERRA_M-T | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 843d7d52-a1ef-3e29-8399-c18445f742af | -11.49559 | -38.48075 | 2025-03-11 12:04:00 | TERRA_M-T | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 30.5 |
| 92b9b971-09c1-3469-ae2e-1080da935882 | -22.74323 | -42.4366 | 2025-03-11 12:06:00 | TERRA_M-T | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e8fd2acd-cf7a-3912-a35a-6e3d3fc8df00 | -17.45288 | -43.64608 | 2025-03-11 12:06:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 615be1ce-5268-3732-83ae-91fc579b2763 | -20.24581 | -41.46326 | 2025-03-11 12:06:00 | TERRA_M-T | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 702770cd-908d-3c37-a41c-be1a2af2b7e5 | -17.97878 | -40.20654 | 2025-03-11 12:06:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| fab9d607-1cbc-36a9-a628-cbfa6b0f01c0 | -18.87192 | -40.60539 | 2025-03-11 12:06:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a0bd16aa-2eb3-3222-a4c7-18b230dbecc9 | -14.4408 | -45.3957 | 2025-03-11 12:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d54f83c6-f285-365c-b3d4-825893714f5e | -14.4408 | -45.3957 | 2025-03-11 12:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8c1d6267-cb1f-3ed5-94f1-379d7b68e025 | -14.4408 | -45.3957 | 2025-03-11 13:00:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ec65de12-0866-353a-ad85-74da0a3b701c | -14.4408 | -45.3957 | 2025-03-11 13:10:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |


