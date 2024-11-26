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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 458f0436-b717-3e20-9608-13db1aca85f4 | -2.08719 | -46.59921 | 2024-11-26 12:53:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b01ddf61-2e4e-3329-99a8-9b7291090155 | -3.72693 | -50.1928 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 0950d609-ab6c-35e7-b727-c0086ac5590b | -3.45195 | -42.08448 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 3f9422f4-9ae8-3c22-b2ce-09815bd7634c | -2.94185 | -44.92311 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a4f38025-2627-30a7-b53f-f8a34503a39a | -3.27389 | -51.26505 | 2024-11-26 12:53:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b9afdc4b-c953-3eb7-a527-0de85b5ae1c3 | -6.65725 | -47.30562 | 2024-11-26 12:53:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 266563af-0fe9-3f2f-9ef2-47dede5f6fc4 | -3.09912 | -41.98948 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 669.5 |
| 3747bd62-ca9e-3134-9e4b-01db87838e88 | -6.84099 | -50.41959 | 2024-11-26 12:53:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3ae42cd1-1a14-324b-a420-e9dc0c642c59 | -3.57687 | -41.93813 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 184.4 |
| 82817e2d-0485-355d-b068-92a8334a67c5 | -3.0603 | -53.2697 | 2024-11-26 12:53:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 894e77b4-06db-36e4-8d04-24eebcad2b53 | -3.33433 | -42.17863 | 2024-11-26 12:53:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 50.2 |
| e4c3f746-2daf-3aa7-88db-385d082d3f20 | -2.1938 | -46.36423 | 2024-11-26 12:53:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 9fc26d8d-8eb6-3f15-b406-b2fea76b71fd | -1.17569 | -47.53806 | 2024-11-26 12:53:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a0742dea-41ab-37be-8de2-44755154d976 | -3.97576 | -48.08157 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| d2809d68-a625-3007-8625-e3535f5e36b8 | -3.0675 | -49.19858 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7a0b513f-6d5c-30ca-be49-fa4f56dc955b | -3.50315 | -50.46109 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 46dfac9b-8658-3a3f-9901-4cf130f38f5a | -6.13009 | -46.90899 | 2024-11-26 12:53:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7d1ec0e1-d0ba-330c-bf39-9f7fdcf44495 | -2.93343 | -48.01844 | 2024-11-26 12:53:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| cb2358f4-e8a4-3b9b-aa04-41be0063b769 | -1.65613 | -52.42628 | 2024-11-26 12:53:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ce131a6f-46bd-3914-ac1c-9af321973bab | -3.57159 | -41.93183 | 2024-11-26 12:53:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 238da26b-323b-347c-a95c-39ef1f49e31a | -5.50323 | -47.65044 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 65871919-7e36-3962-be7f-bc99f1ba4b36 | -4.02958 | -45.53931 | 2024-11-26 12:53:00 | TERRA_M-T | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ef0774cd-8acb-38e4-8b48-a5bcb6826c83 | -3.09303 | -41.98202 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1c9ac697-8929-3e65-b440-f5f04ad0cedf | -3.05112 | -42.35 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 289d80b4-b989-3b5e-ab6e-be8b361e99d3 | -3.58239 | -42.10752 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 845fccc7-7e43-3aa7-aa8d-057f30a848f8 | -4.26089 | -48.66489 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 24bfa833-e256-3972-bb00-8236aff75afc | -3.28968 | -51.15842 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| aa7a10ba-b0ae-322d-a6d0-4840962741cd | -1.57758 | -48.65221 | 2024-11-26 12:53:00 | TERRA_M-T | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b7d7427b-beeb-38e1-a4cf-9fd5ebdf70e1 | -2.94675 | -42.56156 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 38f74e13-3c3a-38f5-97f9-c5df54ddfe25 | -2.94406 | -42.56676 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b96c1b0f-9764-3287-be23-38e8d2ddd261 | -5.44327 | -43.23729 | 2024-11-26 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| ef982cea-de88-3f80-be6c-4a859ce6fa01 | -3.96938 | -48.0618 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 71ba4b41-dab7-3996-8cbb-7ff32ed28ec3 | -3.45834 | -50.83034 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dbbfac85-f831-3482-a64e-cf98dc6c01b4 | -3.97843 | -48.06301 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3faff41b-4ea0-3442-b6dc-2d77d959e619 | -1.86252 | -44.82507 | 2024-11-26 12:53:00 | TERRA_M-T | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dff8f88c-b8e0-3703-818d-7f5ea11b8da3 | -3.46284 | -42.05546 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 3dfdc4d7-a12b-3f81-a3a8-e70f1fc67736 | -3.73532 | -49.94912 | 2024-11-26 12:53:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6f517f36-4ead-3cbe-942a-5e5d5c094e42 | -3.0898 | -42.00511 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 5cfddaea-aa88-3144-8ef6-806186686e72 | -3.32707 | -42.17202 | 2024-11-26 12:53:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2974489a-f15a-3ad1-9e98-b2d5dd932c33 | -3.58214 | -41.95781 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 4ac9dfba-2552-326c-a72e-a2005d0f597b | -3.39117 | -44.17554 | 2024-11-26 12:53:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 432c1144-4c90-353e-97fe-25d2fd49d78d | -1.21846 | -46.32842 | 2024-11-26 12:53:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 8aac882d-96ae-3216-a1cc-9e776a55faa8 | -3.08839 | -41.96437 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8a148e15-0b76-3d76-94f3-32b9ebfc2561 | -1.30693 | -47.653 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4ebc1a5-d3e7-3a28-a353-4bb4fe44012e | -1.84704 | -47.74648 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3452bd81-fb69-3535-9084-0274daac9b77 | -1.52343 | -47.68605 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 1b1a0c5d-2bd8-314a-88b3-f07461c125b4 | -3.57366 | -41.96231 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| bd56af4a-3be8-3406-bcf4-fcddc4ea0594 | -3.27332 | -48.98923 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5689b59c-1f3b-3b14-89d6-e6a8cd7c41e4 | -3.59822 | -50.37925 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 04a478a2-0123-3329-bf38-7ad07207be81 | -4.07357 | -46.54339 | 2024-11-26 12:53:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 74592046-c0d2-3da5-9a0c-54c8f773227f | -2.07768 | -46.59789 | 2024-11-26 12:53:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 5e5bd3e8-a703-3039-9e5b-c028c2e8bbfb | -3.16698 | -42.37131 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 377f3e00-c234-3aed-90ed-da7732e94b70 | -3.9268 | -50.08804 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d10e77a8-90b7-3707-8ed7-54b7dae9b508 | -2.59119 | -47.44668 | 2024-11-26 12:53:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d833301e-3a5f-31e6-ab51-37b8af3acc37 | -1.21699 | -46.33882 | 2024-11-26 12:53:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4794df9c-9d03-3e0d-92f4-6ae3d7d44df8 | -3.97709 | -48.07232 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4e259204-24bb-3096-8184-186706b8ef5a | -1.30563 | -47.66213 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 190f4887-be97-3c7f-aed1-7e680bb27507 | -1.73211 | -46.30164 | 2024-11-26 12:53:00 | TERRA_M-T | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 54a67c66-304b-34b6-80ba-5352d0e3c02b | -3.64392 | -41.54319 | 2024-11-26 12:53:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| a4e75506-3b4b-343b-845a-3f1085ba8e4a | -3.58555 | -41.93369 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| c245513d-9c60-3891-93c0-74d8965c8873 | -3.10917 | -51.25896 | 2024-11-26 12:53:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 44cd8858-7741-3a65-abd9-b5543a153ef3 | -3.39333 | -44.15984 | 2024-11-26 12:53:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| fcea67f6-c284-3eba-a10a-03beb33dd8b8 | -1.47092 | -52.29146 | 2024-11-26 12:53:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 53fa054e-6028-358e-8ece-7de7e4fb711d | -2.88501 | -48.7331 | 2024-11-26 12:53:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| b57dabde-a364-3151-bfba-b9607066d950 | -4.38922 | -47.77099 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 14e9fe40-43bb-374e-acce-92f86916f826 | -3.40182 | -41.4165 | 2024-11-26 12:53:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 8770ceba-1fed-366e-a62c-36d541cb4896 | -4.66854 | -47.94084 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| da8110c5-bf6b-3a10-bfda-b0b757b7355d | -3.68418 | -50.22628 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ac4a0b2c-e983-3224-8e09-2892f6a2e589 | -0.3729 | -51.53947 | 2024-11-26 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 66f6f344-97c5-3691-9f4b-1ae589cdb9b8 | -1.92528 | -50.58458 | 2024-11-26 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 11b05083-6af9-3c48-94c4-65495ad2b52b | -5.45355 | -43.25902 | 2024-11-26 12:53:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 78928172-4193-3fd2-9923-6d9f56b2f1ae | -3.18491 | -42.23896 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 1c4a1a92-02ab-3dbe-9b6b-862c50599423 | -3.96673 | -48.0803 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 46af14de-f5e8-3982-88b4-71b89b111ae6 | -4.45724 | -41.96792 | 2024-11-26 12:53:00 | TERRA_M-T | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 87739910-e18b-3be4-bd83-1fc738c7c10e | -2.34777 | -48.43153 | 2024-11-26 12:53:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c9747e9-f10b-3575-8139-1b256250939a | -2.34906 | -48.42266 | 2024-11-26 12:53:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfb0ae4b-e2e4-3e44-bd69-778ea66e29cb | -3.65705 | -45.06927 | 2024-11-26 12:53:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8cfb5a03-39ee-372a-9402-2a73fc1abc9e | -3.9707 | -48.05254 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 33217773-0e31-3eb8-8162-804514cb5170 | -1.06204 | -48.01133 | 2024-11-26 12:53:00 | TERRA_M-T | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af10c824-80c4-3635-9d22-c1462985a3e6 | -3.94243 | -47.99173 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 62e5c490-15c9-3ebc-957c-f8031e2e779c | -3.97443 | -48.0908 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 9db235e7-8560-31f6-ae5f-69101a2ecb9f | -3.11016 | -41.96031 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 76822c42-eb83-39c7-8944-996b0b787628 | -3.16881 | -51.10916 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1d12f00e-075d-38db-8557-dcb0c198e55e | -0.3574 | -51.99306 | 2024-11-26 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fd9ae524-15fb-38ff-8151-5f6a9fa97ba3 | -3.03915 | -48.505 | 2024-11-26 12:53:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f6484f4-845e-3215-a5bd-e168d28f2ad4 | -5.53672 | -43.41777 | 2024-11-26 12:53:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 646247e2-0644-3a77-bc05-d4588efced6d | -3.32389 | -42.19497 | 2024-11-26 12:53:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 59.7 |
| a015795c-2838-343c-9021-56290e224100 | -4.2596 | -48.67386 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 72f904b8-29b3-393c-b7ef-72335cecbe4a | -3.33131 | -42.20164 | 2024-11-26 12:53:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 0b85ce4d-5021-307a-aeef-545f4f35f28e | -4.45296 | -41.96181 | 2024-11-26 12:53:00 | TERRA_M-T | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| d327b4d4-6f88-3755-b34c-a22249afbbd9 | -1.13479 | -48.33541 | 2024-11-26 12:53:00 | TERRA_M-T | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 840add03-e8db-3569-9612-4624a2e75a70 | -3.94375 | -47.98241 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a47cb8b2-4ea7-3253-8262-b0cdcf8656ed | -3.05402 | -42.32824 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3376c0ee-4317-3819-9ce3-78c984aad43b | -4.53946 | -42.95304 | 2024-11-26 12:53:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3894b384-1b13-3d2f-97d8-e82ffc02eb19 | -2.08569 | -46.6095 | 2024-11-26 12:53:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ba3422b6-330c-3932-8665-0d9fa98b0271 | -1.86062 | -44.83828 | 2024-11-26 12:53:00 | TERRA_M-T | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 860b68dd-ae23-3b63-9611-24923e3ab19a | -3.4996 | -42.04338 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| d7613357-c71f-335f-91bd-c6fcd341a696 | -3.09605 | -42.01261 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 330.3 |
| 05ec10c8-1a54-3c45-a879-9a9cf7154513 | -3.64736 | -41.5174 | 2024-11-26 12:53:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 404df68f-4265-3ff3-bc26-d0895d1496c6 | -6.12857 | -46.92004 | 2024-11-26 12:53:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |


[Clique aqui para ver as próximas entradas](README48.md)
