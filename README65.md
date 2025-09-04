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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eb5396d-3d56-3713-a439-a9f4e53bc9c5 | -6.16011 | -43.31859 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a815030f-286f-36ac-bb11-3ff2a4259ae6 | -8.87382 | -52.02976 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5076cd2-56f0-34ee-ae7f-3e2b0b8612c5 | -9.64997 | -48.04227 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173fae04-ab1f-39cb-98b3-a07ab58c47d4 | -6.54572 | -43.91507 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 720c3d76-e1e1-3497-9368-b7733c954e2a | -9.97793 | -51.63276 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0550c3b0-9114-3495-a1fc-775549f4bd9b | -6.83783 | -59.15197 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35421765-530b-369d-858a-992a71b5bb8c | -5.30533 | -55.97651 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f2cae90-6e5b-375c-9187-340564997032 | -11.05195 | -45.40427 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 808c1705-bf27-3dd8-9ff4-c9cec3808a1d | -6.78772 | -44.0847 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c4fa1abf-af49-3ddf-82e7-b92ff46e2f30 | -6.78122 | -44.09332 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 913b65d2-b594-32d7-ac36-894271228914 | -6.24458 | -42.63911 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 583413ae-9c95-36d3-9e14-e10dee8869f4 | -8.02876 | -44.14253 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6145fabc-4d2b-3b5e-972c-832a0c5f6541 | -9.96426 | -51.63066 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4164e900-7a7d-37bf-b161-5290280ead80 | -10.44311 | -50.26453 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2119ec3d-3752-3359-8021-732935588262 | -11.05496 | -45.14522 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c3972c6-779d-3985-a4bf-3fa39e2ff115 | -7.07702 | -46.19444 | 2025-09-04 04:53:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ee2a409-f350-3772-b655-6972cfa128af | -5.92504 | -45.55432 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29580218-1ec6-380e-97b8-04f4735a58a0 | -5.74845 | -45.54499 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27eea63e-47ed-3b0f-9018-97fb753324cc | -5.86625 | -46.11979 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bfc4d23-6146-373e-8df1-dd8867879bdf | -10.42702 | -50.37406 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 35199fbf-95ee-3227-a5ac-f65aad9ef441 | -5.3016 | -55.97591 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b24d97-40b1-39dc-886e-0525cd5afcfd | -6.89182 | -45.55989 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c3b65be-6cda-353a-a55b-40808217fc28 | -4.99968 | -56.259 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 87a79477-93de-3212-8446-4e8aa4c7fb59 | -9.46846 | -47.6047 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d949d8a-d9ef-3e6b-a7f6-779fb8873a4f | -7.92963 | -44.92814 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7f280ff-31fa-37ca-9dbe-53ae6d97f958 | -14.99495 | -50.07035 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6ca311a-7e78-31c3-a877-04ea34d061bd | -13.74178 | -46.93787 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 310786a3-680b-3420-9c4b-cb1225d1a104 | -15.0159 | -50.03341 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a158c156-17df-30d5-acad-3e8a73b5db1c | -14.28594 | -45.22875 | 2025-09-04 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 794e4d68-f11e-3056-b3df-87b885216f3e | -11.67991 | -57.3483 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b5d7a80-e52e-3ebf-be26-08cd92e9a7d1 | -14.90563 | -49.62687 | 2025-09-04 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb512125-c406-362e-b1b9-dc45f6419d7d | -10.46667 | -53.62866 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe138801-bc62-3d9e-9be2-64834694317a | -11.09217 | -52.02498 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a56ce497-514a-3559-8e7d-e35c9a3399f1 | -13.10545 | -57.11936 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23e5ec6e-dd42-37e2-b7fb-365aeeecf965 | -15.02305 | -48.10497 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15949786-02a8-34a3-9a73-1239e2bec84c | -12.91607 | -56.99863 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc2df1f-ce6c-3497-be17-52eb342f0392 | -12.96639 | -54.77422 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f48e442-6603-3c4c-8367-ada941ac845a | -14.58262 | -54.57257 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dca67f29-9498-3e33-80e4-13375d5cfb2a | -11.64277 | -52.21033 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3946ec14-6911-371d-a1b4-0bf273d69fbb | -14.54015 | -48.05415 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49cb1d35-b120-35c3-b57c-fda031a97ba3 | -14.77421 | -48.13844 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d08f60d3-2a6f-3ba0-bbcb-f5eaf5b2be76 | -11.20084 | -55.01621 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 477f67b6-d414-3641-aeb0-35c62fb40f13 | -14.99561 | -50.06553 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f05e6c9-b582-3ce2-975b-94b81a846872 | -15.1727 | -52.35801 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0dbf7400-94b6-3c24-9850-abc5738e5093 | -11.84299 | -51.44577 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e7b7607-3179-33a0-928b-549bb2119d4a | -15.04883 | -50.05368 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 912a2381-ac78-383a-a8f8-e3640d6a6112 | -12.18258 | -53.88124 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| addf1f3b-dfad-3a0e-9f91-b42396a679bf | -11.5837 | -52.11847 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a8a673a-02ce-3347-9a4f-e7201d2b25cf | -10.94697 | -50.98851 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5d48a71-6dd6-3474-8627-fe5ea0613c88 | -13.4557 | -46.83228 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afbd911d-87f6-31c4-a90c-66419e2c1b4f | -10.47886 | -53.63783 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 215dd7f8-a3fb-3f50-a783-8027634bd487 | -11.64221 | -52.21402 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b877629d-b6a5-3421-8ec2-e55fcd01c3ad | -15.98432 | -55.96019 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f5957724-f456-3bc1-bbef-a1cc7ef05681 | -16.5551 | -55.10391 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5e466185-48c5-30d7-bc61-f6f61765c492 | -12.62371 | -56.98859 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c266ea9-4a2b-36a2-b8d0-f58fcbdcdcaf | -15.47266 | -53.015 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3542dea4-5edf-3594-977c-d6d4f2166769 | -16.53247 | -55.07411 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e6271b01-7f69-3c68-bf42-6b5acf647e31 | -13.73488 | -46.91753 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 396acf26-30db-3736-b08d-38e143470ca6 | -16.54178 | -55.10161 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ee44941-cc94-39a3-af64-da28ad070a97 | -11.86732 | -51.52948 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85171976-f70b-350b-a979-7a9441dd7a5c | -11.85971 | -51.43629 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5109201-cf0e-34ec-80f8-b1b7fc1ca330 | -15.00661 | -50.07202 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51ae1861-ed4b-38af-bdef-b64cba2d9e51 | -11.64333 | -52.20663 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dcce1a6-e217-3d31-bf6f-c0c074b54e04 | -14.57225 | -48.04833 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7fb726-11bb-3b60-b108-c974082fc4fc | -10.09494 | -54.76909 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012e9b4b-e6bc-37a9-8270-7d76dc76aa4c | -16.81705 | -51.32823 | 2025-09-04 04:55:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1baad154-dc7e-3ae4-a472-fd1b1f36870e | -14.82189 | -48.21457 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd57f6cc-3c97-376b-90b7-d72d54b2014e | -13.85873 | -47.97928 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6bf828e-fe7d-3b6b-b475-a83c5f901a18 | -17.04012 | -47.14145 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49f740a4-349f-3142-8a15-e921cf7920bd | -13.57016 | -48.1324 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 184486bc-0bf7-3027-8ba1-c29529be6e38 | -15.75936 | -49.97799 | 2025-09-04 04:55:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 67b7aa35-b79a-322a-894c-2ed6a539f8c6 | -17.14925 | -46.24949 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4192dfc1-be63-3ed9-b033-0f7bafd9a07c | -14.53733 | -48.07565 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de9b336e-b797-3a4c-8468-7afa8d8929ed | -15.00471 | -50.057 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c17bf590-cfd5-3275-b712-25af2f08798b | -12.48618 | -53.83982 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe14f00f-7844-3fec-b7fb-72624b919a13 | -14.39215 | -51.67356 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe70c31a-c647-3589-bab2-3562a63cf3e8 | -11.61664 | -52.1766 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2429d8e0-8e0c-30a9-9bfe-dcd6dbca0592 | -11.78093 | -47.32887 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b8ad6a4-8eca-38ef-9d7b-f043051e9d3d | -15.53502 | -51.72009 | 2025-09-04 04:55:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c0c3650-8310-383d-83c6-6164413bc2a2 | -11.88591 | -51.54815 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7506736d-b7ac-37c5-96f5-374ee661ecdc | -13.9949 | -49.55918 | 2025-09-04 04:55:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af59966b-10c2-313b-811d-9377c92cf081 | -13.43685 | -46.93058 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a231be7-bf06-3b34-be0b-4000671c8f33 | -15.13936 | -52.33341 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c85cbf94-86a0-398a-9ab2-9ec76685885d | -11.20243 | -55.02771 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3377f701-74a8-39b8-84d0-a6fc1d1ca0d7 | -15.33445 | -47.35714 | 2025-09-04 04:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a568db0-92ec-3db3-8a9b-082464e052b9 | -17.17374 | -46.23006 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8761b73-f65d-375f-9267-eb48e10e6cb1 | -9.81972 | -54.87369 | 2025-09-04 04:55:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6fcb338-d642-3532-bdca-e654cb9c573b | -15.19749 | -56.36421 | 2025-09-04 04:55:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b811b484-03eb-3d63-a6e1-5274b59d6b88 | -14.81909 | -48.23612 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c93ab92-54bf-354a-b922-468dd43e0a14 | -12.97203 | -54.76049 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e2255d0-288c-3d5e-b6c2-a78e88d2721e | -15.1515 | -52.37119 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b1a1aa5-da56-327f-ad04-8276bd9aac0e | -12.49838 | -53.84907 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88880fc3-dd5b-32e2-8de9-e68571fa791c | -12.48007 | -48.07609 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ba82a10-9ea8-3b9f-80eb-5230a501aad7 | -11.19347 | -55.01873 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed97938a-dd47-33e9-b985-dc1010ae8248 | -12.87477 | -48.02254 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 025c141c-3ae1-3ff7-8d08-599966518121 | -11.59111 | -52.1613 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 317df842-2c8d-31b4-aab2-47b694a979af | -15.46016 | -53.00533 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18f8080-759a-32e7-a057-b921ed8f4fae | -13.86365 | -47.97563 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba44ef17-5d52-3653-8d02-3522903eedee | -10.53008 | -57.77579 | 2025-09-04 04:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6543715-31dc-3b09-9ed7-a9f7db025686 | -13.88953 | -51.81454 | 2025-09-04 04:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README66.md)
