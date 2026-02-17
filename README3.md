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
| 0048bbb2-aa69-32e4-a6a8-9f75d5b05b5e | -20.45868 | -45.57346 | 2026-02-17 04:18:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f2d85ec-1465-32ac-b4bf-b9c0798476a6 | -18.97018 | -52.92839 | 2026-02-17 04:18:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94d45488-fae6-35b8-921c-5e2c628bddc9 | -17.68136 | -47.86877 | 2026-02-17 04:18:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3120c238-5394-3ded-8cc3-d42c939f9d8b | -16.02734 | -41.18581 | 2026-02-17 04:18:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 878b59c9-ebc6-3a0f-9c93-c5365dd1e3cc | -17.96705 | -44.93184 | 2026-02-17 04:18:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31d3e5ab-4a64-3e50-a896-9c4538e2aba7 | -15.89227 | -43.47688 | 2026-02-17 04:18:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 46b7cafc-06b2-35c6-b9a6-568ac0da9d83 | -19.95473 | -49.4203 | 2026-02-17 04:18:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4445c9ae-6454-3d94-8c4f-11c2aca7f0de | -15.89568 | -43.47742 | 2026-02-17 04:18:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f9259cfc-ed5c-3411-8e37-294c12210b0e | -18.81064 | -51.61048 | 2026-02-17 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2351d235-3712-3fc3-8990-d0c24b8bf457 | -16.60991 | -43.36123 | 2026-02-17 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7e98f6f-71d9-3123-bb64-5d26688c1fbb | -16.65066 | -41.96452 | 2026-02-17 04:18:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5b3aa9d1-cbaa-3b71-ae93-e23af281edca | -19.26223 | -49.35985 | 2026-02-17 04:18:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 537f6df4-04f6-3a10-bbf7-dccadb8c5a59 | -16.65437 | -41.96481 | 2026-02-17 04:18:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6eb658a1-36a8-3849-975c-ebd48af60f80 | -17.61259 | -46.65393 | 2026-02-17 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 890a298b-c002-3fd9-889f-d5e6c212a84b | -19.17123 | -50.49276 | 2026-02-17 04:18:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28aa409a-6280-323a-889d-0f6d03247f56 | -20.46144 | -45.57779 | 2026-02-17 04:18:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8104d39-8f61-3429-a04b-a926db8c5f09 | -17.654 | -47.75716 | 2026-02-17 04:18:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d37b2d3-1064-3dd2-865b-bafb14af4a3f | -17.61318 | -46.65029 | 2026-02-17 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1a8bcd6-aab8-3a1b-bda2-71c064a78456 | -20.45812 | -45.57719 | 2026-02-17 04:18:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a93f11-9e23-3211-94de-025d4dad4961 | -20.76059 | -44.02775 | 2026-02-17 04:18:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b41adb56-2168-3008-9dfe-7bad5ab1de4e | -17.58822 | -44.49256 | 2026-02-17 04:18:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90413c10-b289-3188-91ad-9d4073401d57 | -19.91819 | -44.68487 | 2026-02-17 04:18:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc734469-00cb-3312-9980-bfe7bfa58d5b | -15.17284 | -45.64287 | 2026-02-17 04:18:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7ee6d7e-ed65-33e8-b572-ac47c57f5619 | -16.39005 | -41.05011 | 2026-02-17 04:18:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc85c420-a137-35d1-83fa-5b0f424821a1 | -19.04195 | -52.35607 | 2026-02-17 04:18:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2d46335-1da5-3a6c-8067-405c9c8d3197 | -19.04099 | -52.35899 | 2026-02-17 04:18:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28397afb-8790-32f6-95ac-dfe586668df6 | -19.16567 | -50.60849 | 2026-02-17 04:18:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d8a9ce5-3ba7-347c-aa13-4acb7c01950f | -18.97456 | -52.92936 | 2026-02-17 04:18:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 496ecfeb-0bc9-3192-9af2-bb8a52344162 | -19.1717 | -50.49049 | 2026-02-17 04:18:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4bf03dc-8a46-3085-9114-34dce2dd1229 | -21.7805 | -49.8289 | 2026-02-17 04:21:00 | NOAA-21 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aa6ebca8-ce39-39ea-9a14-508a7420da58 | -20.30137 | -49.58535 | 2026-02-17 04:21:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25c0c6c-c3e9-34cc-8e46-4b550bb863e8 | -27.82939 | -50.30331 | 2026-02-17 04:21:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de22435b-0345-3d8f-885e-8d4a538817a2 | -20.78586 | -49.58125 | 2026-02-17 04:21:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 032c00d5-f0b9-3b96-ba90-dba37e63747b | -22.31993 | -47.14909 | 2026-02-17 04:21:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 234e21ca-f402-3b92-b800-c8b7c05b5e7d | -20.62722 | -47.07063 | 2026-02-17 04:21:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 808492a6-664f-395e-b909-a909be5d2fa8 | -21.14933 | -48.59557 | 2026-02-17 04:21:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a0abaacb-bdf7-3fec-a14c-cf127d3263a1 | -20.30492 | -49.58605 | 2026-02-17 04:21:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf40f415-ef82-320d-8163-16a5086ca476 | -20.78232 | -49.58058 | 2026-02-17 04:21:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fc9fe16b-2ce8-3b68-bf8a-bfd8c6fba961 | -21.37299 | -49.10547 | 2026-02-17 04:21:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 707f5fce-c29f-3a6d-84b4-7286a3cf325a | -21.71174 | -48.43538 | 2026-02-17 04:21:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a6421f47-93bb-3679-8c92-c62876136924 | -20.30776 | -49.5852 | 2026-02-17 04:21:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c2c542e-f52c-31ab-a2be-35eaf49857e3 | -20.78661 | -49.57698 | 2026-02-17 04:21:00 | NOAA-21 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b7c63896-7a9b-3d0a-9f27-cd52c51c6761 | -21.78403 | -49.82959 | 2026-02-17 04:21:00 | NOAA-21 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e499a08-abfb-343c-b732-4eb23786e3fd | -20.84315 | -51.73685 | 2026-02-17 04:21:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b197dcd8-5dcf-33b3-8aec-841ddfd4a792 | -22.48253 | -49.26632 | 2026-02-17 04:21:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e57b105d-0131-3a49-a634-b21fa3ed6bf3 | -22.07905 | -46.90769 | 2026-02-17 04:21:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cad96200-245e-3170-8654-e0360a6b17ed | -22.25261 | -48.11789 | 2026-02-17 04:21:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5cd87a9-a127-3920-97ef-a73071b23c6b | -21.18725 | -48.57846 | 2026-02-17 04:21:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4aa9804c-b4b2-3da2-9dfa-7ce07a0a3577 | 3.18341 | -60.5085 | 2026-02-17 04:42:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35a4ed7-9d50-3ca8-8f67-3ce36a32a415 | 3.18432 | -60.51493 | 2026-02-17 04:42:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fe6dcb2-6ac7-35ff-985a-046253f40c4d | 3.18627 | -60.52017 | 2026-02-17 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32177668-d5a4-32c6-bc26-b0c386fc2e56 | 3.18436 | -60.50731 | 2026-02-17 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee4fa1d3-12fa-397f-ae67-2f2d500a8ccd | -2.94516 | -39.94968 | 2026-02-17 04:44:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ab41d584-0630-3790-98c6-6af62d0b29a9 | 3.18531 | -60.51371 | 2026-02-17 04:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31564077-70a6-3383-ab32-17b787abcee6 | -11.71098 | -44.72846 | 2026-02-17 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5411632a-a596-3fcc-9ca0-a3cf97b86d27 | -11.94261 | -44.80737 | 2026-02-17 04:46:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9892697d-b413-3d53-b7e0-7eb7c9573cc4 | -11.71217 | -44.7309 | 2026-02-17 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 796ce636-5c16-3a49-81c3-770ec9a9fccd | -11.05548 | -45.38597 | 2026-02-17 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5fcacff5-b84a-340c-bb07-64d7f2e51b41 | -11.88647 | -45.28529 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 728b1ff5-15af-3ab0-93cf-e8e55635425c | -11.88544 | -45.29284 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b73d9a2-0633-3b12-837e-2bdb1bda457e | -11.88751 | -45.27768 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5221df9f-4c81-3fb8-b1e9-17f6a96ab7c6 | -11.93831 | -44.80676 | 2026-02-17 04:46:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff4b8c64-855f-314a-acdd-0d4c4c0efcf7 | -12.07537 | -45.34932 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 467026dc-9a74-34e9-9f88-8413e592284e | -8.06515 | -43.15199 | 2026-02-17 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e972029-d9a7-325e-b7e3-ad9b7337c57e | -11.17918 | -43.30527 | 2026-02-17 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da8c25df-7b38-387e-b0d3-3bd1f88215f2 | -11.05496 | -45.38963 | 2026-02-17 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6317947-b2ad-3a1e-a878-d36b836b718c | -14.84284 | -40.90711 | 2026-02-17 04:46:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b311e8a-5868-3c91-ac28-69f8662e98b4 | -13.43705 | -48.22588 | 2026-02-17 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6118588e-49e5-3b61-8738-2720822eedf9 | -11.7104 | -44.73257 | 2026-02-17 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2628147-fc83-34a9-b6dc-e53df4164757 | -11.88129 | -45.29214 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ddcd338-8043-3322-96fd-f93265c42d3f | -11.88595 | -45.28907 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32654252-42fb-34fc-a502-ea28c2212c7d | -11.88699 | -45.28148 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43d7e4c7-5c2a-31a5-bc3f-a44e6975b82c | -11.88232 | -45.28461 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6cc49cd-4e03-34fb-a2d5-cd0aa7134bfd | -12.24195 | -44.23489 | 2026-02-17 04:46:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a56e755b-cb05-357e-b625-b49a35687531 | -11.89011 | -45.28972 | 2026-02-17 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06b36edb-35d1-35bd-b4c4-6447da5ee0c9 | -20.75692 | -44.02713 | 2026-02-17 04:48:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 97a81467-bf4e-30b4-8750-58e6c5adb804 | -18.97495 | -52.92958 | 2026-02-17 04:48:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fbba5494-cbad-3bf6-ad0f-0ef1da43144b | -15.95689 | -53.36974 | 2026-02-17 04:48:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c49749e-433d-3c5c-9359-b2caf4a29164 | -20.45689 | -45.57797 | 2026-02-17 04:48:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f87713cd-160d-3b97-a187-99c9a0dd49bd | -15.44171 | -43.63945 | 2026-02-17 04:48:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7d394d0d-fa12-33b2-854c-fd557896422f | -18.97828 | -52.93018 | 2026-02-17 04:48:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08360ce4-d892-3bfc-b5c7-ded501c907e3 | -16.44882 | -58.1804 | 2026-02-17 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0cb5c4e6-f82e-33c9-bfd7-7d3d1bc22af0 | -16.02595 | -41.18551 | 2026-02-17 04:48:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d0d7993c-4a50-3480-9431-82498dda975e | -20.45748 | -45.57298 | 2026-02-17 04:48:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca4ef9b4-6da5-3874-9e95-fd9d3c94f1aa | -16.44962 | -58.17618 | 2026-02-17 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23698416-f1c4-37fb-9e79-e1781393e92a | -15.17429 | -45.64376 | 2026-02-17 04:48:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aec9b81-97c8-3139-8331-9c5b0c796fdf | -17.3869 | -56.9686 | 2026-02-17 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94733b46-e0a4-30d7-8bcb-96d7836936e1 | -16.02554 | -41.18927 | 2026-02-17 04:48:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b524e8d6-c6db-324a-aa7f-8bb48f47026f | -15.17003 | -45.6432 | 2026-02-17 04:48:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecc4c4f7-add1-3bc8-96c4-9616971682e4 | -15.89711 | -43.47937 | 2026-02-17 04:48:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0322d52f-e52e-31da-b8cb-432b45e909c5 | -15.89213 | -43.47872 | 2026-02-17 04:48:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 83614561-18c1-3578-9be0-c00e6c83fbfd | -18.97162 | -52.92899 | 2026-02-17 04:48:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d214f50-b04c-3f93-8129-3c54b285de8a | -20.76203 | -44.02779 | 2026-02-17 04:48:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| d80abcc4-19c0-31bb-bf66-e85fe9037003 | -15.16951 | -45.6472 | 2026-02-17 04:48:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ad1529-dcea-3bc5-88e8-1141f2d8f936 | -17.61321 | -46.65425 | 2026-02-17 04:48:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bd2407c-defd-3638-997c-1d8d54887fb6 | -16.70067 | -48.18967 | 2026-02-17 04:48:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ce3cd40-8129-3e5e-8e3f-4a32a9332a9a | -17.95649 | -54.49944 | 2026-02-17 04:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97cff225-fc5c-3b59-b8b4-1b848b80500a | -19.04189 | -52.35871 | 2026-02-17 04:48:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcca6a9f-ee74-37ed-af2a-5bcc9ef5b289 | -19.95246 | -49.41959 | 2026-02-17 04:48:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb226e93-0ad4-3157-bd98-e307660c777e | -17.67877 | -47.8685 | 2026-02-17 04:48:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README4.md)
