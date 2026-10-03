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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aae867b4-90f1-3161-8c80-8af2ed45af7c | -2.02407 | -54.30762 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3f7ab92-88f8-3739-8f06-6536837af4fc | -4.24201 | -48.67685 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11ed27af-ca00-358b-9d50-0c238999f8d6 | -3.26584 | -49.52324 | 2026-10-03 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034f8d8d-27da-3438-a872-11d07935519d | -2.87229 | -50.32034 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b5f4014-2f65-30b0-99e9-8ef8c442ff5a | -2.90718 | -54.12884 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f638993-3c42-38ad-9a33-26be4bcf055d | -4.18813 | -48.67197 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50ab78f-65e7-3303-aec1-57b69fd69248 | 0.62633 | -54.40862 | 2026-10-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca065111-0135-397f-9e0a-0d6c3be5abab | -3.18329 | -54.09905 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d0d4eca-703c-3e03-902f-16e541e6a2f4 | -0.36478 | -52.01975 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e482fcc-2c4d-3373-994b-4db878b36c78 | -4.04779 | -51.08826 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2c158ce-0b64-3ae5-8372-f5bcc83c7d78 | -3.01119 | -53.87184 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09f6af19-78ba-37fe-9a05-a26ce9aecb87 | -2.97493 | -54.09579 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6606643d-0442-34b8-9cfe-377b44785d90 | -3.12991 | -53.73458 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5a596452-fd87-3406-b3dc-2abfb7a1d700 | -4.18866 | -48.66852 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ff2ebd-942c-3356-bf46-3d4926c40ddf | -3.71266 | -50.65761 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4afe1d46-23ba-3f46-af42-1a90885d391b | -1.15194 | -48.9624 | 2026-10-03 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 615280d3-228f-3b7e-b671-7b5904a2f2bb | -2.92052 | -54.09743 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e73820ee-9d07-30e1-9893-c4ed0854af96 | -3.2288 | -54.31229 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68db3c34-887d-3585-88f9-6458fcde76da | -1.0854 | -54.1053 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e8947bd-8492-37fe-9f97-b52ab588a44e | -4.29052 | -48.56055 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7acf59a9-645d-3419-a112-70189dfc24d5 | -2.89139 | -54.14893 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778b24e1-3ead-364f-9219-ae109d457a32 | 1.78476 | -55.59236 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b11bc57-9d62-3c75-9829-b724002f8045 | 1.91562 | -55.77859 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f168b668-737f-3aef-ba99-99c2b49ce95e | -3.17518 | -54.09763 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8da23c3b-dde1-3242-aa1a-ee2f54cd0081 | -1.73758 | -57.17406 | 2026-10-03 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99bb9aca-61c6-3b1a-977b-c0cc6eb8fc7a | -3.82013 | -52.20467 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187554f9-2843-3eff-b587-0275293b5575 | -4.35817 | -43.83072 | 2026-10-03 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ef046b9-4acf-3a76-9891-4bd90ba987a8 | -3.01987 | -53.89463 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7fddded-5f8c-31f9-a834-a66e95127846 | -2.57049 | -54.74556 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 878b82c1-e83a-3b63-9e4e-ac0f3a55f9e1 | -2.17848 | -49.77322 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e57d8376-36cf-3b0d-8b73-53bc3963f883 | -3.17924 | -54.0983 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbe15a57-4aa5-33e1-a9d3-8a80e969fde9 | -3.00662 | -53.87465 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0870f694-e7b8-3a09-a5b6-04f6e454915a | -4.45676 | -47.9234 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 80c3bae1-7e9c-39d3-baa8-6b16d98e0836 | -3.28893 | -53.82668 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83fe0589-2e62-32fe-b336-a1513cab3f95 | -1.68851 | -48.2035 | 2026-10-03 04:38:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16732c76-d94e-325e-b3cd-7da3b313a0eb | -3.32217 | -54.17024 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e22f4d0-192d-3fb4-b791-37d8607d8c98 | -3.55649 | -52.25172 | 2026-10-03 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 346c789a-7e66-3043-a89a-018dc37b6892 | -3.12936 | -53.738 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff86f02a-5e9b-3fd4-ac37-bfa928d732db | -3.28439 | -53.82957 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 044437c8-321e-39ce-8aa3-647f1d5e0694 | -3.1037 | -51.2837 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61b4080b-32c5-3743-90fd-45cb29b9e24b | -0.90794 | -47.90889 | 2026-10-03 04:38:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecdf0b3-63e8-3b12-94c9-c78a51eb27b1 | -3.12198 | -53.73332 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c852efd0-1192-3b5f-8025-6189cbf73b0e | -2.98479 | -53.26468 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ed64ef1-834a-33e3-b540-0395e5eb70fb | -3.12427 | -53.74422 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a47a6580-4dc9-3384-9374-e4e8448cf0ce | -3.05635 | -54.1605 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16da5558-9fa4-35fb-93e6-8ffed7775148 | -3.22404 | -54.30846 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c22c7b94-21fc-306d-bf50-6bfe89aa721b | -1.08312 | -54.11348 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e887a370-7d14-319e-ac66-a4a3e3010bc3 | -3.12539 | -53.73737 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ec7daa8-2485-311a-913d-c454bc29308c | -3.51351 | -54.60514 | 2026-10-03 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c9309be-f719-3a9f-8fdf-fe45f6b35fcb | -3.13444 | -53.73179 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 02167b75-a109-3a4a-8767-6212466ef8b7 | -3.77003 | -51.86061 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27c14214-5f0d-363b-8088-96dfad4ef351 | -2.04909 | -56.86798 | 2026-10-03 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3290da5e-135d-35bf-a752-f4856d167248 | -2.89257 | -54.14157 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0dc8c6b-f747-3461-94ff-09bb1ba7bf57 | -3.28784 | -53.83358 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc086b4b-10b9-330a-a706-533cb1a1aa7a | -0.49948 | -49.10785 | 2026-10-03 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d2f53a-ac1a-3c02-9569-8df7397f0afb | -2.88788 | -54.14465 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97f4cf2b-e358-3e88-a034-4ad625e7e290 | -1.10563 | -54.14 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93615d3c-af97-317f-969c-81816e8f14c0 | 2.35064 | -50.75189 | 2026-10-03 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63de41f6-3f90-30e7-9cf0-e9d1d441d347 | -4.18482 | -48.67145 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94176db6-4c39-3fba-9e98-89562c033bbe | -3.92136 | -45.78051 | 2026-10-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba2b697-5e3a-3e21-abe3-446989ce664b | -2.27943 | -45.24574 | 2026-10-03 04:38:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fd1d224-deff-3972-87ad-c0a5c68c747c | -2.56827 | -49.11033 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07f58b8-d5aa-325b-9525-316142263ecf | -3.43718 | -50.66298 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da601685-f896-355e-bddc-6e24c19029fb | -3.21137 | -50.91433 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550e9116-7992-39c1-8301-5f9eec70c42f | -2.95751 | -54.07451 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc9879d0-d19a-3d31-a2da-47dc708273f6 | -3.35066 | -43.38313 | 2026-10-03 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afb0afac-581e-387f-b0af-00b2cff3149c | -3.11553 | -50.28146 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b3016c6-02e6-346b-bf5f-e06a9c8f0cba | -3.42059 | -48.33625 | 2026-10-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59e74777-ad88-39f6-acdd-b7f72431268e | -2.78468 | -48.6595 | 2026-10-03 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81be2518-257e-3e85-8ac9-4ab90d1130b7 | -3.13841 | -53.73242 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85da1466-bb29-35a9-a335-b336a40724cc | -3.10769 | -50.28755 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f69755c9-7de3-36eb-83d4-a1bf6a77784b | -3.21537 | -50.91115 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cdc41d9-3c44-3be5-b1ed-bad038b8fa54 | -2.24981 | -51.93237 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d692a839-75e3-35d9-900d-e11f611e733e | -4.60603 | -46.78409 | 2026-10-03 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4af1cbeb-8207-3c21-a131-0c18e531cf15 | -2.18957 | -46.57153 | 2026-10-03 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ebb122c-2133-3674-8170-f52ee8da3c8d | -2.25343 | -51.93294 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed63680-6eb5-398e-8b08-164eb01dbcd3 | -4.45359 | -47.92688 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c4b68e7-6af8-3bc4-a4b8-221aebdd3e6c | -3.50384 | -53.20557 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8006ff24-d929-3542-bcd4-0a771f15c61c | -1.18782 | -49.2969 | 2026-10-03 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8144be17-5211-3ac9-b327-1e4102d9531b | -2.91068 | -54.13315 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7795d899-214c-347f-858d-331d65ba8a1b | -2.86153 | -51.01771 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38c57422-a03e-3193-b8a7-0d43a15683b4 | -0.40811 | -51.98577 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfd9cb20-6f4f-3fc6-907e-a529b16899e4 | -2.8914 | -45.40846 | 2026-10-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b08f5ff-174a-3735-9eb4-44604e5eac15 | -3.2833 | -53.83643 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b93de069-a3db-3c8a-a40a-f104c730e528 | -2.9246 | -54.09807 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be65ff42-f6c0-39a9-9727-0c43667426f0 | -1.44567 | -48.90936 | 2026-10-03 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0018baeb-e338-36a4-a2f5-083c7a049445 | -3.70928 | -50.65708 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b38838-4244-37f9-b402-87b844c3d90d | -3.29019 | -53.84459 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ead9999e-49b1-32d9-94f5-b5b942c6a33e | -3.10441 | -50.29437 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54012724-f1d6-3ff9-9992-efb3385b0368 | -3.29074 | -53.84112 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62558039-50b8-35bf-a496-da21d0056957 | -3.11974 | -53.74702 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63277c63-7c76-3c8f-a807-12e4ba0446b3 | -3.32405 | -51.67588 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ed24281-2089-3bdd-b4e0-6e34c6b8ea77 | -2.99943 | -54.23072 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d9537fe-274e-35a9-a02f-1a1766e8529c | -4.45731 | -47.91985 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad31c11-d8d5-3485-9d25-cd969028d28c | 0.69802 | -51.43326 | 2026-10-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08c49d4b-49ae-3b3b-8412-d9bae8855366 | -3.22527 | -54.30797 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7f7ff14-911a-3939-9fdc-e9adac60496c | -2.60621 | -48.25548 | 2026-10-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2aa4c7f6-1835-3d90-894b-0fcb73b6cf6d | -2.57832 | -50.00137 | 2026-10-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107ea78e-fc5e-3537-9056-5f784f94887a | 0.62259 | -54.41357 | 2026-10-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c485d14-c02b-3904-aeb4-af1389394eb7 | -2.88044 | -51.03214 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
