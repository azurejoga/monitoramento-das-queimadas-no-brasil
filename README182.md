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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b12bc8-9404-32df-878a-aff61029b979 | -16.47666 | -57.30109 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5e349777-4277-30d8-8568-214e1624a344 | -16.47632 | -57.30416 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 40fe6f1e-3ace-3e2a-90a6-371eead80727 | -16.47598 | -57.30722 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aecdae5c-7ee0-384c-b297-debb2f0898fd | -16.47593 | -57.35365 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b4141599-3828-337b-94db-62fbb65be71a | -16.47559 | -57.35668 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 15fbff13-bc30-3e82-a0db-851da2a50bd6 | -16.47529 | -57.31336 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1060ec3c-2ec8-3284-9bd8-59aa5d85add8 | -16.62909 | -57.21618 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b2733d41-a80d-3af6-8c9a-6c6ca596fd2d | -16.62874 | -57.21931 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 52bf7786-5127-3808-914d-df9e5c8b9bf7 | -16.62838 | -57.22242 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5f347fc4-ba2c-39fa-92b4-57e79c149a1d | -16.62397 | -57.21555 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 516f4790-dc5c-355d-887f-f00404a50871 | -16.62362 | -57.21867 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 76397021-5ef0-364b-81b3-93780a98ce89 | -16.6185 | -57.21803 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0e8edb96-f9c7-3f67-b9dc-03a2a63befa1 | -16.61815 | -57.22115 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 995b69f6-3fa3-39b9-96f7-01ec20080ce2 | -16.61304 | -57.22051 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 15cdc1d7-c0e0-3697-af68-762f1a62964d | -16.61269 | -57.22363 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a1566695-26d7-35e5-a2f3-c2e36b3beae8 | -16.61234 | -57.22674 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d6df4f94-8848-34c6-9678-631acecff674 | -16.61199 | -57.22986 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c30072fe-1de5-307d-8372-263d32e2fece | -16.61164 | -57.23298 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4cac08cb-df53-358c-9c88-058dfa4004e7 | -16.61129 | -57.23608 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 58bcb105-66d4-3955-826a-f83977aa96dc | -16.61094 | -57.23921 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| de8464b0-8537-3b4a-927b-16a39a8b676e | -16.61059 | -57.24236 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1ef87323-f7a4-3f35-a7a5-d23c3a353ec1 | -16.61024 | -57.24551 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| dda5a537-9c2b-34b1-8072-e17e143b254c | -16.60954 | -57.25168 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 982f4a6b-6c63-3b4c-8231-33e5cfc383a4 | -16.6092 | -57.25475 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 414d086b-ca60-3a5a-9a07-21c0dacbff7e | -16.60688 | -57.22922 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3432d7ff-14de-3392-a33a-d79118d31f2a | -16.58154 | -57.28596 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 761a2c32-ce32-3450-abde-e55982a03435 | -16.58118 | -57.28904 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 142ba5e5-d0a7-380c-897b-358f301276c2 | -16.58082 | -57.29213 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c38afcb0-1651-3d12-8dd7-79de3f7bd91b | -16.58009 | -57.29828 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 623c457d-1743-31c1-95f5-11e34a4b4abc | -16.5238 | -57.29441 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a78509fd-5d57-38c3-8aec-570d389ab3d4 | -16.52345 | -57.29747 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bb98fbaa-1994-35fc-bd8a-0991b6049c6b | -16.51871 | -57.29377 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c7d86236-9090-3e17-88cd-aa5b4cf2bd53 | -16.51801 | -57.29991 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e66bd2ac-6862-34c4-95bf-67f28fcee9ec | -16.51398 | -57.29005 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a43be864-5a3e-307e-ad11-50eb3b39e187 | -16.51363 | -57.29313 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 34cf6b1e-19b8-3946-9690-18220f58ad80 | -16.50819 | -57.29559 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| da56b81d-82dd-377e-bfc5-5d78f5d854af | -16.50749 | -57.30176 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 65b015bc-0cb0-3072-8993-01fb4dced6d6 | -16.50715 | -57.30483 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cae99389-7981-3844-9cfe-b6b4b9c1e3e4 | -16.50645 | -57.31098 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 67ba7310-31b8-3b29-8deb-6ca26d76b537 | -16.50506 | -57.32323 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cbf62b52-1d97-34cd-8fd8-3be6c896c9c6 | -16.50311 | -57.29499 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 34383bc3-fae1-34df-8d61-d550084721a3 | -16.50171 | -57.3073 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b6820d44-b4b0-333b-a007-d7031796d810 | -16.50137 | -57.31037 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 53c9842c-99da-330d-a81e-b4556ea07958 | -16.50033 | -57.31956 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2b2cc1d0-fad7-3d6d-9713-857fe42cba79 | -11.66291 | -65.20216 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a5f3935-ba47-3757-99ff-1f5ebd1b51ee | -16.49594 | -57.31282 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7fdcae3e-1627-3cd6-a447-d05268dab172 | -16.48818 | -57.30497 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4a3b3943-4757-386c-9a18-e8506aced240 | -16.48716 | -57.2993 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 249838e8-7f07-3654-a136-8ad7d917b9a5 | -16.48613 | -57.3085 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d2ea6787-58a8-30be-b8a5-c907143e7bc0 | -16.48347 | -57.30128 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e9024246-4b50-3d05-9dab-980edea99188 | -16.4831 | -57.30434 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b1432ea5-0b2d-366d-a1c9-55b4050b3887 | -16.48208 | -57.29866 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 14dac2f1-3c6a-310f-b0de-d031df033aa5 | -16.47839 | -57.30066 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 22aec204-0510-32a1-af50-d81e51cdf0e9 | -16.4773 | -57.30985 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9790f731-07ac-374e-91be-b4c2f7fcd0b1 | -16.47693 | -57.31291 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f351fe9-a86c-3964-b6e3-6987136b6e0d | -16.47657 | -57.31596 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e5155985-4bf5-3eb4-af03-3ba024be0847 | -16.47621 | -57.31901 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ac708577-c67b-383e-97c7-268b59c72a56 | -16.47584 | -57.32206 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 029d3816-faa6-3fe2-852e-69e6536e3e27 | -16.47564 | -57.3103 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f1cbb4f9-9650-3a0e-9a31-abfce133f9c9 | -16.47222 | -57.30922 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 37b915bd-7c47-39cf-b2c7-80e861f7ac19 | -16.47186 | -57.31229 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bd1dfc1c-3059-3b07-9cda-c21f68572195 | -16.47077 | -57.32146 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cfdaa859-4fe0-3d3c-be39-aa7dff834ac0 | -16.46642 | -57.31472 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5b7df20f-9ae3-3af0-9443-0e7c802c6354 | -16.46606 | -57.31778 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 19bec968-c76d-3e2c-b3ce-044b0fd8e214 | -16.4657 | -57.32083 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| df896e2a-60b3-3f7f-ae7b-bc2b7577172a | -16.46063 | -57.32021 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cc21f2a5-3b38-3e81-a11e-c89d9ed7c6fe | -16.46027 | -57.32327 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dbc824c7-df55-3e93-874e-f0a29a0bd0be | -16.64447 | -57.3528 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00d9bc15-44e0-3075-80e7-6b86267e3bf9 | -16.62856 | -57.357 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0c0397bb-e6a0-32d5-99fa-3164bd3ff485 | -16.6282 | -57.36006 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d92d532-bc3a-346b-8ff7-14e7f5648acf | -17.13502 | -56.73701 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 274fb4cb-c016-3b6b-8556-6041a340cd18 | -17.13463 | -56.74044 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 89746f42-d67c-3c9c-9660-9c3bd3245fbe | -17.13425 | -56.74387 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b2aa2ffa-c61f-3c71-965b-a9d5816a98ea | -17.12931 | -56.73983 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 655cd662-f1b0-347e-bb3e-f6a5acdb5b49 | -17.12894 | -56.74325 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 39693272-a738-3fb0-9b1c-e3c17cf08bb3 | -17.10767 | -56.74074 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b20af7de-3781-3a07-8f00-9e604f8758ed | -17.1073 | -56.74416 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7f4b1361-618b-336e-9a46-1129228c547c | -17.10693 | -56.74758 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 23a21e7a-b15c-340a-b8fe-bcac4bf5092e | -17.10656 | -56.75098 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 275013ee-54ed-3deb-9c5e-244bbf751936 | -17.10618 | -56.75439 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e45291cc-78ed-3346-ae05-1d5b68a97ea8 | -17.10581 | -56.7578 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fd123c9e-5256-3dad-9d17-4920e83e5e86 | -17.10544 | -56.7612 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3652a369-ad8a-345c-8cdc-a4ac954aa2f5 | -17.10507 | -56.7646 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 32c428ac-41b2-3595-8ee8-f410b8234d3a | -17.10162 | -56.74694 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 357a5ea5-49ff-3d0a-9b30-346a1cbe19f4 | -17.10124 | -56.75035 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6af732aa-b3fd-3f6b-ac13-8fadbd69e28e | -17.1005 | -56.75716 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3159fb2e-fb41-3bb9-9d8d-d79f2e2a2a9d | -17.10013 | -56.76056 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| df4d58d6-59bf-33ff-84d6-af65198f610f | -17.09976 | -56.76395 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| da71e088-0b24-32c8-95c7-3bba9c003d7b | -17.09939 | -56.76736 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 293fe5da-f3d2-33bc-b70b-5cc863b1e194 | -17.0963 | -56.7463 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 03d0f82f-ce00-395a-9d0b-6aaf8a4f1422 | -17.05314 | -56.70926 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94fbb18b-816b-3ccb-84f2-d42ad2bc50a2 | -17.05275 | -56.7127 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 240b0267-90c8-3d1f-919b-3c2fa2ba84eb | -17.04776 | -56.75702 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5cedc2d-6015-3a37-9d56-0ae7bffe9f7e | -17.04738 | -56.76043 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 986fe908-4280-3c10-b772-5e02c380dffd | -17.047 | -56.76383 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| df2be9b9-fae5-329d-ab0d-a25724399c92 | -17.04399 | -56.74278 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d7f10db-cfcd-3e8b-bb9b-2684c5bd05c3 | -17.04361 | -56.74619 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 096c8537-b001-3d09-bc06-6bc61f47dd2a | -17.04322 | -56.74958 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cc7b43bd-2b8b-3bfa-abdb-27be35d8a353 | -17.04284 | -56.75298 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1e096851-9f44-3c6a-bc8c-59e6134477f4 | -16.64515 | -57.21184 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README183.md)
