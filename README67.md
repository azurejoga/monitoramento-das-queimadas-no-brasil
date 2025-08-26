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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e84b46d6-344e-3b20-887d-f82c66cd961b | -15.11277 | -48.65358 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c605fc6-96f1-3234-9aaa-be5595e5f86b | -11.30148 | -55.10978 | 2025-08-26 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e261749b-ea2b-305d-b5d6-51a62995436e | -13.40807 | -46.89794 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80cf2eeb-c697-3e8a-aab2-02ed6e9f5805 | -9.103 | -62.67257 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63dabd38-b380-3ab0-8272-c7f580d03409 | -14.58655 | -54.51209 | 2025-08-26 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0ea28aa-89cf-370d-a70d-f60d99c26d12 | -8.99277 | -65.41219 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29ede77c-ba75-3f79-ab34-b9c1dede211a | -11.5542 | -52.12286 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5954153-45e9-323e-a252-7c93577e44b9 | -9.17797 | -60.8596 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 684ac7b8-ad09-399c-8a11-10d485459043 | -9.17962 | -59.44722 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 93a79a47-7bbc-33e3-9acd-51fed6ebd35e | -11.55807 | -52.09828 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043e1813-0551-3328-bb39-1b121fd3d9d7 | -9.41173 | -48.25045 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b33f199c-ff71-36f0-9a83-bb386f36ac20 | -11.5084 | -52.13345 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1410d7a1-97cb-37fe-be93-adeac2b472d8 | -13.44437 | -47.00846 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3514bb2-7c4f-3c73-84ec-075a1d93bba1 | -9.16599 | -59.52157 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41278a2e-73b6-3c48-aaf5-0c3b837a3d15 | -14.30929 | -53.06456 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2094c773-b0f3-3428-942b-202f8752e111 | -9.18442 | -59.44807 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d869b870-e240-32a4-9dcc-deb8e520abd1 | -12.67635 | -47.86493 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 62412b39-fbec-396e-9c8d-2d2a84014985 | -9.18362 | -60.79956 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8905cbf8-9663-3115-9568-cc27964a89af | -9.23223 | -60.92162 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8b42bd8-faa0-3b78-97c6-3cdc75048dcd | -13.52316 | -46.90731 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f634b51-6e23-3fa0-9ddf-1682bf6cbf97 | -9.18346 | -59.45334 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5b748eeb-3c37-361d-9acf-5ebad3035ab6 | -13.5084 | -46.88902 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac813d97-547e-3bdd-8f02-51acc653605f | -9.07763 | -62.67672 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2da2e8f6-977a-37fe-a83b-6c97c5c093dc | -7.40313 | -64.35504 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ca67b0f-93a7-3f33-af84-fb8c2ad0c458 | -9.14806 | -60.78621 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f6f4035-7e9e-37af-b224-8ba14c218aec | -15.02057 | -48.51191 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 354a4d6e-7194-3c74-b39e-bca40083a47f | -13.41926 | -46.87878 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4ee4c8e-8bc2-3352-860e-d35e7462d6a6 | -11.63626 | -46.4063 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68d5b9c3-69a8-376d-9037-030906b6628b | -13.52639 | -46.91529 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8b08d4f-6c31-3531-b9a2-29ae60883b65 | -11.55185 | -51.8776 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fbbb781-fe13-3428-9327-31948ff45b8a | -8.32636 | -50.57456 | 2025-08-26 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e07fc16-8afa-34f5-b4c8-7fec8b751b33 | -8.9014 | -62.46914 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| efca1f4b-4949-3e6a-b488-166cb8306a13 | -7.38966 | -64.35238 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73b72d47-ab25-3818-a770-aed572449bb7 | -13.41506 | -46.878 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0240096-f5a5-315f-9bae-89ac426f3739 | -10.41782 | -64.39922 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab1c0b4a-6e26-3031-90f3-462f5514c801 | -13.43727 | -46.87294 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb647835-539f-3e21-9b70-b9119529442e | -12.74354 | -48.09564 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 972ba7d3-bf89-3bb9-84d9-95e021e83955 | -8.87022 | -62.44088 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21b0aad9-477b-376f-8e5d-23c429cc51d3 | -9.58155 | -55.37038 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 84657631-8076-3497-b9d7-dbb6a08adcdb | -11.10604 | -44.75565 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a42932d-828a-3664-8695-c43015a52887 | -9.84759 | -46.45812 | 2025-08-26 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e955d8c8-25d3-3d42-b3d2-f1bb3d5d5d6b | -7.87486 | -63.01653 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 276582d7-8d23-361a-b8f1-6aba7cf020a3 | -11.53133 | -50.45373 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eac617c9-ce8a-362e-9be8-b73969344248 | -7.37829 | -64.3655 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcb590a7-0491-3353-b967-fd46276cc99f | -13.52216 | -46.91476 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1246d825-1189-3541-bc75-6e2b933d8948 | -7.41826 | -60.62408 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3453abbe-cade-3e1e-9be7-deaf9504d9df | -10.86807 | -55.79438 | 2025-08-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3203cdb9-c767-3049-97fa-c7c7c7b58a58 | -11.51116 | -52.1375 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3540890e-ae40-35d0-8df6-1d87335de60d | -8.9748 | -65.42968 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b2852a8-6ca1-38d4-90f5-4642865740a9 | -9.06066 | -49.55833 | 2025-08-26 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ea61aa2-e237-3251-b199-9746ad8907bc | -12.94061 | -46.34081 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a76c030-dd4e-3056-87a8-c5eb4da5dd10 | -9.16208 | -59.54293 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78accece-7617-3bf2-bdc6-94a226580f27 | -15.08688 | -48.55394 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe7b5099-8736-3a2e-8328-d54b5b76bb9e | -11.63573 | -46.41024 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e90e74aa-b43d-392d-a833-4e5a67130f03 | -13.0378 | -56.84869 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc193a64-b3d7-3a8c-9685-3dd632a99c3b | -12.76885 | -48.121 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9fe3937-f9f2-3f63-9ba8-781e14fca747 | -11.52164 | -52.13559 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 75e08bc9-78e4-3647-b429-5f244384e9d5 | -11.15537 | -44.75817 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fabbafe-6d61-3c85-a116-ff1ab1400abb | -13.58899 | -48.19862 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e61ea61-7935-3c81-93d7-8f0db58b8164 | -11.26519 | -44.99465 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cecfec0d-9686-36e0-8ed8-92f269e75bde | -7.05142 | -59.19691 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f1d7644-4a71-31d8-bfc1-f4b8826ad216 | -9.17896 | -60.79539 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f014ae-eb24-3b83-8bf5-beb5c72cb09a | -8.57348 | -62.64127 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c733fffa-fc36-3ed7-a7b0-04a99bc003e6 | -8.8455 | -62.45358 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6762f7f3-5a6c-3101-80c8-bb656249e0b1 | -9.17756 | -59.54015 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4a4484d2-5db3-3aa0-87dc-7c63839974c1 | -10.41787 | -64.39828 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12361200-28a3-30fb-a7fc-7f23452ea9db | -10.03317 | -59.35723 | 2025-08-26 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d424cef-2568-3939-a5de-3878f6a8a6a4 | -15.05579 | -48.69628 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6baafaba-12aa-3130-9a2f-d4e3d7aa5a73 | -12.9417 | -46.33269 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25542b2f-9dfc-373b-8aae-f351d2d844bd | -12.44147 | -43.56653 | 2025-08-26 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29064dec-6843-303d-8517-eb10d77b36c4 | -13.43824 | -46.99813 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 187fa59a-8184-3b26-a55d-8a9dc4c37be4 | -11.0597 | -52.00744 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3a621b0-e172-3326-8886-b8ecf1070449 | -12.49138 | -53.82856 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ebd073-5493-3755-a0a8-418aa01bc000 | -7.53519 | -61.38716 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 141905bc-a5d1-3325-aa86-884c3b45da2c | -8.84432 | -62.44905 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d674fdbd-0c32-325b-8dc2-52315a4193d6 | -12.73573 | -48.16119 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fd84ded-d411-351b-9b69-9bf4656ee851 | -6.81535 | -59.43287 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d92def45-81a3-3d0b-b1c5-3a1b992c407f | -12.73045 | -48.15943 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3522c85f-86f9-3f79-abc1-33985c941faa | -11.40438 | -58.53814 | 2025-08-26 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d78eaba8-31d5-307b-a584-bbbdbe2357e8 | -8.88804 | -62.47541 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa7ed82f-fc12-3eb8-af21-51ee3b577229 | -7.37385 | -64.35194 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1525f34d-05cd-3323-b90e-7c0a5007855c | -14.9698 | -50.17027 | 2025-08-26 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc541ea-12e1-308b-b6b4-50adee3cd884 | -15.18037 | -48.19003 | 2025-08-26 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f42542ba-0c7e-393d-a604-e19da00329fe | -9.17919 | -59.51134 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03ec15f7-618b-3998-9bcb-409f6bcbe9b9 | -8.53929 | -62.64631 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8db9ecba-78d3-39d0-8a25-3f75d411c0a4 | -8.35043 | -62.94391 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59036c65-101f-3407-b853-b561721ca358 | -12.67676 | -47.86267 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 84371cbc-187e-33d1-a9ad-4c6317ec69a4 | -11.15338 | -44.77371 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| df318441-5341-3ef0-bd19-97ba40506446 | -11.54593 | -52.13232 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0d09661-cf48-398b-996d-b59b501fb1fa | -9.84345 | -46.4576 | 2025-08-26 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82197170-1c18-37de-9005-0415f02b7f0e | -12.72804 | -48.14879 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 818a5cec-fd49-37f9-9848-5e284ffabc27 | -9.2181 | -59.67671 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8818fb23-394a-3412-b491-a19347231089 | -8.99144 | -65.41895 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76697246-5f28-3b91-a39d-2286ea28fe45 | -9.1611 | -59.54827 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f5a71c3e-b4de-38a3-b43a-78d4cccb91bf | -9.15392 | -60.78393 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d702757d-4c8b-3b12-9176-c65c757ce03e | -12.77085 | -48.10654 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95603a75-b238-3356-bfc7-94d50401b036 | -13.5205 | -46.89517 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e469968b-97ab-38d4-8f40-c4c64e86e8d9 | -10.41892 | -64.39376 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e6acf81-1307-3c3e-8f91-cb54a7766101 | -10.41467 | -64.38161 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff034843-a649-39c9-993c-96a4b561a766 | -12.66747 | -47.8716 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README68.md)
