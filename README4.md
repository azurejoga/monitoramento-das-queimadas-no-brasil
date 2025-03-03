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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df8e8cd7-fa4b-3b83-829b-c34406110667 | -13.98158 | -45.58613 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| faa474fd-0acb-3e77-99a3-11c1b8b23b88 | -14.45826 | -45.64489 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a24d79e5-54bd-35c6-9a69-ac803c5ec61e | -14.00132 | -45.57879 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| efb84094-34bc-3b2d-be38-4898bae552fa | -19.02104 | -57.62334 | 2025-03-03 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5563e0a0-d309-3eb5-aa05-af81fa0cfd4c | -14.00594 | -45.57941 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 69e363ce-1198-30be-930b-0dc307431817 | -14.45362 | -45.64426 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f742950-e372-3a2e-b7c9-42323d558143 | -14.45912 | -45.64814 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fbfb8ee-c884-3f1e-bb58-7c661b005470 | -13.98282 | -45.57635 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70834c7e-ac57-3d35-a199-6df2e8479a4b | -13.99019 | -45.59227 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fe34e15-a62d-3348-87ac-41aed9129971 | -14.0093 | -45.58983 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb3ad3d4-b6da-3c20-8319-055ef98edd42 | -14.00804 | -45.59962 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b55fdaa-f284-3b76-8775-7493fa697d6f | -14.00069 | -45.58371 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 79351cb4-7d4a-3833-9144-5a73a2763f07 | -13.98495 | -45.59652 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64748de9-ce35-37aa-9b60-a8c0a9996660 | -13.96094 | -45.56335 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b39b066-3d38-3ed7-8093-7838dca57f28 | -13.98096 | -45.59101 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7ba77f3e-53cb-343d-b3cb-7382428e0a8b | -13.98682 | -45.58187 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f1f7af2f-3626-32c4-a1a9-8062ba99ecf0 | -15.80193 | -47.99838 | 2025-03-03 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae3c7986-e258-371f-acf1-c59552df0010 | -15.79789 | -47.99782 | 2025-03-03 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b8c5ee29-0a24-3c18-80f6-f2de7f70700a | -14.00867 | -45.59473 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3475f5f3-0a0b-3a8e-bc0c-80c12728b0e9 | -14.45765 | -45.64983 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1912459-b610-38a1-8f02-f6443e15335a | -13.98557 | -45.59164 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58b8d026-67f7-3dce-890e-b70cdb69d244 | -13.98957 | -45.59715 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 376600ac-dd98-3cec-ab9b-5b15d556dd64 | -13.96618 | -45.55909 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 737392d3-685c-3749-a404-2634e2f7c04e | -13.98619 | -45.58677 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e86b3a25-b289-34ef-822c-79806583db51 | -13.96156 | -45.55845 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6fe55df-cffc-323b-a7b5-d6bc68e51554 | -14.45449 | -45.64752 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98bafaf7-87d6-304a-9c56-342e1a6b5afd | -14.00195 | -45.57388 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8eb003fd-054d-3efe-9dfb-7a7c2a1c7d6d | -13.95693 | -45.5578 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e96d9e4-3554-3554-acce-cb13c44c9e97 | -13.98744 | -45.57697 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb2526d1-80a5-34c4-96cc-b5dccaa43440 | -14.00468 | -45.58922 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b022b2c3-61dd-3631-a779-f41f83497009 | -14.00531 | -45.58431 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 93857e2b-c0e4-3c3f-838c-a25d7edf56c2 | -13.98895 | -45.60201 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9778f6b-e795-3429-b92e-929d8400c134 | -14.00993 | -45.58493 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5f1e7fc-833f-3f4e-994c-92e3a11ab648 | -13.96495 | -45.56889 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d29739a7-1c67-30f4-a434-6c040c1dce9d | -14.0072 | -45.5696 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3c3654f-b55b-3b4d-bf0c-37c324544329 | -13.96557 | -45.56399 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b64b993d-50fd-3d89-aa16-5856bb7f3645 | -13.98034 | -45.59587 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7c643846-f97b-34af-a16d-168da96fbdbe | -13.98433 | -45.60138 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 386a9cf6-a739-377d-9c88-08060a52bc0f | -13.97019 | -45.56464 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0786713f-c908-39bb-ab2a-9f6bf89d9b76 | -17.39765 | -46.56189 | 2025-03-03 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fc6a096-8a19-3dfd-a539-4a4a884150d9 | -14.00405 | -45.59412 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fc55c00-310c-3ca3-b47a-e8b032534ffe | -13.96217 | -45.55355 | 2025-03-03 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2edeac09-513b-3dd5-beca-cfab683517e3 | -24.58751 | -52.8217 | 2025-03-03 04:48:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61157312-e099-328b-9454-3679444ed45d | -24.18466 | -52.79772 | 2025-03-03 04:48:00 | NOAA-20 | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f719f9b-f632-31f2-8530-56338728853e | -23.83136 | -46.86342 | 2025-03-03 04:48:00 | NOAA-20 | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ecc9a75-82b1-39ae-94ad-9519b1dae2f5 | -24.24306 | -50.73943 | 2025-03-03 04:48:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fb9eb175-0439-34b7-8c7d-a18094383073 | -23.59264 | -47.44036 | 2025-03-03 04:48:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e72851a-d80b-3525-b81d-b21b7ec96a92 | -22.23415 | -56.81733 | 2025-03-03 04:48:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53720905-025b-3a70-ac93-a0a1d72ee1c7 | -22.68299 | -42.8921 | 2025-03-03 04:48:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c9095393-54ad-3c11-a1b2-e4c62a62557d | -22.90917 | -42.84988 | 2025-03-03 04:48:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a175e4d-444a-3edf-bc84-19565c321be5 | -21.22984 | -56.06151 | 2025-03-03 04:48:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 052ea689-26dc-3778-b499-f63b31204e85 | -20.7147 | -54.41719 | 2025-03-03 04:48:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1482ac6a-517b-3132-835c-f93ea3a63803 | -20.71139 | -54.4166 | 2025-03-03 04:48:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6c3b126-9c39-3256-8b0a-3dcc022dee41 | -20.71801 | -54.41778 | 2025-03-03 04:48:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f5c50e7-a8e2-3da8-a26c-a330b62934a8 | -21.79894 | -54.60711 | 2025-03-03 04:48:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60d8be40-ac5c-32aa-b552-7128d55acdda | -22.91524 | -42.84769 | 2025-03-03 04:48:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| dc3e6031-b3fd-3f79-a439-111164f623dc | -22.91534 | -42.85041 | 2025-03-03 04:48:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2fb70e83-4fb8-3cfc-b93b-b8f0e4580b73 | -27.14155 | -49.45685 | 2025-03-03 04:50:00 | NOAA-20 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86e5553c-6821-3322-90ee-7d3d6b076d59 | -28.58675 | -49.4422 | 2025-03-03 04:50:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 62201d80-ead8-3f99-b674-00c450b59228 | -30.43251 | -53.51107 | 2025-03-03 04:50:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| af9d4217-4403-3ee8-a9e6-535170a3f8df | -27.37963 | -53.93511 | 2025-03-03 04:50:00 | NOAA-20 | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 11f2c43c-eb76-30f0-b975-076d5435ad84 | -27.37906 | -53.93281 | 2025-03-03 04:50:00 | NOAA-20 | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e6fd7880-2607-3905-80ed-52d4a185f756 | -27.0399 | -51.40209 | 2025-03-03 04:50:00 | NOAA-20 | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f8de9e3a-de36-305d-96fa-c2b67376bc12 | -14.0029 | -45.57409 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 2422ea06-fcb6-3cdf-92b0-6cf09c660ce9 | -14.01036 | -45.58454 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c4af1e3f-eefc-32f2-879a-89aa53b8d0a4 | -13.96894 | -45.55949 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a7150e4-336b-3940-a629-aa6621a9aca5 | -13.9601 | -45.55812 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2747211-fb84-3e40-b8b0-98ee88ab1195 | -14.00153 | -45.58315 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3e838b9f-10b8-318a-8b76-1014ab9e8f76 | -13.98386 | -45.58038 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fdae214d-8904-348c-b2a8-f14ae7af3427 | -13.99132 | -45.59083 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 88831c09-49bc-325c-bb24-a31e9debf114 | -14.00899 | -45.59361 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| df293772-7eec-325a-aa18-a344a0bf8980 | -13.96148 | -45.54906 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed04c075-094a-3d26-93ec-a6e93e9861db | -13.98523 | -45.57132 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0e20eba9-4d32-32c3-8a04-32b615d8a72d | -10.50328 | -42.3944 | 2025-03-03 05:25:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4a52d1ff-16bb-3aba-8ba0-05e0f0a7e0fb | -13.98994 | -45.5999 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ba1daf0e-c0a4-353d-8d55-b40207aeba9d | -14.00428 | -45.56503 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5b436b63-9003-308e-92e6-a6360c26e38b | -13.98248 | -45.58945 | 2025-03-03 05:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a9b21c3c-66e8-3dd6-8c6b-c2ec450fe63d | 4.64589 | -60.84793 | 2025-03-03 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fefc66a0-77be-3e1c-9ead-78ac61b8c6a3 | 4.65692 | -60.83218 | 2025-03-03 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f065144-0fa0-3099-b88e-db58ac01e009 | 4.64643 | -60.85136 | 2025-03-03 05:31:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae80285-53f4-3e63-b3f0-ba8afeff317d | 1.67423 | -60.65401 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa21352-e62f-36bb-acb7-42c7853b5bdc | 0.76167 | -60.4358 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7a7f973-c65f-3cf4-9e23-a59d86759385 | 4.005 | -59.7356 | 2025-03-03 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d02befa-f1d2-309a-9ce6-3ba112cbbe78 | 2.024 | -61.4291 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da3f059b-17ed-31cc-8943-8e898b20d79e | 1.93538 | -60.39143 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| efb7a751-775b-31e3-af1c-e8b396b01ffc | 0.82399 | -59.26906 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 801726a0-9c61-3562-8b62-815de522d8ef | 2.11251 | -61.82239 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50d8b516-def7-3b91-a93c-82e7b139cadf | 1.83678 | -60.64704 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2adbef47-7d1a-333d-902a-12adba2619d8 | 0.96138 | -60.53019 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785ad86c-b3c9-33a9-9bef-41d38c223116 | 3.20586 | -60.52323 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb68624-8ff5-306f-b8a6-abdd5acfef37 | 3.70575 | -60.75899 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf77e4da-5d4b-36a9-aca1-7e7720e0743f | 1.88235 | -60.3518 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f61151f-b8b0-351e-afc7-7fa20219bcd9 | 1.89861 | -60.38957 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81a3c2d7-9bc4-3e9c-b17a-5ad37b044f3e | 1.77768 | -60.37911 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36622648-5417-300d-899a-9b60cbb6ca55 | 0.96206 | -60.23713 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c780c40-4d88-3fb4-9e32-dd11ca084213 | 3.36229 | -60.08949 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0627d010-9751-33fb-a0d9-28f1cd397f76 | 0.85909 | -60.59422 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 261fd902-1888-3608-97f4-171cc901d31b | 2.7622 | -61.42564 | 2025-03-03 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2a1c37b-ab25-3911-b528-d5fe1af19391 | 4.23735 | -59.85061 | 2025-03-03 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbba3b97-e074-3e53-a017-c4aeaceef650 | 1.58212 | -60.2021 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README5.md)
