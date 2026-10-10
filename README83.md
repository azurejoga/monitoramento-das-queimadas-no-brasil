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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15ddd2f2-08fc-3627-8cfd-7ce27700a2bb | -8.35695 | -48.14188 | 2026-10-10 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79c0f50-053b-34d2-9bd9-2696e7c574d0 | -10.05397 | -44.35164 | 2026-10-10 04:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2255c588-1a02-3628-ac7a-f9476626563d | -10.25054 | -49.66579 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f438a17a-b7f1-321e-9111-b3194f88c021 | -15.10739 | -43.62986 | 2026-10-10 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2014a11-e6e7-360a-87f3-e6c8233a0549 | -13.15817 | -48.14079 | 2026-10-10 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1073574-d9d1-345a-bb31-501149521392 | -9.28794 | -47.39829 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b5d9df9-c0f7-311a-9c12-b19d681540ae | -7.02173 | -47.6864 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55e8bab0-ad2d-3288-b24f-b72e44734c6b | -11.6678 | -43.69767 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99098cd8-51d8-34f6-a95d-e8da6e7f4c8f | -11.20694 | -44.85052 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff78336a-7913-3598-9927-548712283d6c | -12.0037 | -48.16975 | 2026-10-10 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 875ca55f-4731-362f-be28-e775390ea324 | -6.4199 | -51.95402 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9968741f-8757-33d0-a5e8-71bd55b6266b | -9.11224 | -45.82961 | 2026-10-10 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5da8aa9b-9a3f-39e4-a1a1-8cd1c3a75985 | -7.22346 | -55.07544 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11494936-0464-348b-ba66-db6c7640b85d | -7.52775 | -45.31456 | 2026-10-10 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e334bb52-8055-3400-91b5-a2dd96a8e5ae | -15.37058 | -41.93189 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f6c9676-67b0-3074-b78f-eb1308a5af1a | -7.90759 | -54.72977 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bc7ce1dd-9ed7-37f3-b21d-966769d88e74 | -7.26792 | -57.12031 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1044d4f5-7e7a-3f85-a022-5d4835889833 | -9.51505 | -54.67329 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb7e217d-0c9b-336a-9d82-0299fa0c2a29 | -11.8765 | -47.36246 | 2026-10-10 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90f9bb0-5c9a-31cc-bf16-19aef48220b9 | -6.43 | -55.27147 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 345473ec-0d17-3914-960c-258004bf8d2e | -11.02007 | -44.03481 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80871fa8-6b67-3090-9174-c5986582f217 | -12.37274 | -46.61199 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1af98973-2f77-31c7-be4c-d667729fe1e0 | -11.56019 | -43.6895 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f533aa1d-d570-3fd1-9711-53afc081cee8 | -13.67842 | -49.10829 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1ff249c-8ca9-35e0-831d-30f14fde94cd | -7.18499 | -52.62028 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f97f55be-c463-3898-bb7a-e87a2d7b2bc1 | -13.25264 | -42.25607 | 2026-10-10 04:46:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bc1a7bf9-ba65-34d9-9ece-3a3977cb28b4 | -12.03945 | -43.37966 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90750db3-cd65-3945-82d3-64389178070e | -14.05739 | -43.83498 | 2026-10-10 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f362eeae-1d0f-3309-815d-4a3131ace01e | -7.01344 | -47.71719 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c40fdb3-30ac-3b05-96a4-3bbaa2b9fd1e | -8.49628 | -54.60437 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c12e6b0-5de6-3f37-a27f-4b908e07711f | -7.19427 | -52.63761 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| afb14172-5d77-34ab-8155-a4b19d756824 | -10.89839 | -44.80249 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff083fb6-3879-3ff6-a509-003d11560ece | -8.95802 | -47.37979 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11ee2ed5-d079-30b9-8b47-0d7f943bdaec | -6.99458 | -47.70708 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a19402f8-5904-3081-95c0-99c6999d386a | -13.46584 | -41.34594 | 2026-10-10 04:46:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e51cfdc-4a35-3db1-9905-0da773865c6c | -8.18257 | -54.71789 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef26e0bb-7b13-360c-ae8c-fc14517c32fd | -10.60808 | -60.49095 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f07390fe-6150-3334-98d1-cdb3d5a3e7ae | -15.26693 | -42.37568 | 2026-10-10 04:46:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 878d8cf7-227f-32e7-b926-52186554c622 | -6.72284 | -50.94198 | 2026-10-10 04:46:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1060d091-871b-3381-b370-838abf04354e | -6.43884 | -55.22021 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 721cd3fa-fcf8-3463-b4d7-8aa60703f6de | -8.53755 | -47.35389 | 2026-10-10 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d51835e-f040-33ca-b3e9-0ab5696daa1a | -14.24017 | -47.30575 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 358e273e-9565-3bc3-b784-11ecaed40d72 | -9.95998 | -55.33642 | 2026-10-10 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa2b5c2a-1c0d-3056-8c51-abc308562f87 | -6.62388 | -59.94543 | 2026-10-10 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8098b800-fe5a-3944-9c8e-3632104a7c57 | -6.49642 | -55.31204 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e3e5c27-a38c-3b73-bb46-c9198030c227 | -13.73781 | -44.30434 | 2026-10-10 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18de74e5-bc5d-3fe3-860e-44d839217e4e | -7.2356 | -56.4214 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fde9ce3c-2b03-3d12-b008-bb30bd1f43ed | -14.45127 | -43.93502 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02320137-7c23-330a-9fd8-c8b06194ecf7 | -11.56681 | -43.70224 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a6ef220-c641-3049-9d7c-0327b9ff47eb | -12.36982 | -46.60746 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2b4a7de-92ac-3e8a-8870-a98634167b31 | -11.09745 | -43.99021 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1220796c-150b-3ad6-8123-a8900ceeec0e | -7.91576 | -54.736 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8bc55b0-7f90-3b9c-8110-3a9d1df8ef20 | -11.96222 | -43.47276 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8ab7dec-7062-3c7d-b409-720a81fbd055 | -10.41628 | -47.29266 | 2026-10-10 04:46:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4bd5d7b-1723-3af1-88c1-9e6218e8be82 | -11.07154 | -54.51344 | 2026-10-10 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ceb2ed51-b120-3ff5-b7dd-65cd27d329ca | -13.41089 | -43.73312 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2b69cba-3fae-35ae-aeda-9697706d1ae2 | -9.88842 | -44.79053 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd09d2e2-1698-32b5-9df7-21cbe7c65013 | -10.2444 | -49.6611 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87cd5616-cab0-3380-862d-c3bc509d910e | -9.17316 | -47.70405 | 2026-10-10 04:46:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e905b06-687a-3728-b30f-4974bf59bb4f | -10.61005 | -60.48103 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 22fca013-48a3-33f5-aaae-21094ebbe62b | -13.37616 | -43.89672 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acff6d84-ac69-37cf-bfb8-226643459cbb | -11.0819 | -44.11201 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db9136d1-3570-3e8b-9467-ab223c7f4d1f | -11.21052 | -45.24687 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b96ac7a7-890b-338e-9565-87bde85293f7 | -14.45811 | -43.94801 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b7e7e4b-9e96-3398-b4f0-344c4dabc30a | -8.22884 | -46.37302 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 298d1492-4ac3-3763-b963-4edf5409b024 | -11.75613 | -46.79484 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fa90fe8-0518-30c3-bbbb-66fbfc1ae313 | -15.24514 | -41.88635 | 2026-10-10 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ce9efe1-e37a-3245-9740-16acc9d74fde | -12.02804 | -43.46587 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 887c9572-8a97-3624-bf37-7f83dc0ad741 | -14.44287 | -43.93383 | 2026-10-10 04:46:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 860fc95e-c44b-3f51-98eb-478f1e977a28 | -11.86453 | -47.66959 | 2026-10-10 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c61dcfd-e014-3379-9ad4-434c62a00502 | -11.60622 | -43.74901 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25a390e5-12c0-3360-8ce7-9d98a05a2cb3 | -11.75902 | -46.7993 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a090f3e6-1d99-3362-88a6-ff550378ad75 | -8.95131 | -47.37872 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20f1ccb0-9878-3e8d-bd7c-ec5e5cb58e48 | -9.32345 | -47.63344 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241cf612-fa55-3297-935d-154fdb5dbc9d | -13.03654 | -46.81476 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22e0de4d-5e55-3a67-9893-4c8e5895cd9f | -10.6038 | -60.47985 | 2026-10-10 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ede2130d-da86-3132-b5fd-6ba67d8750b4 | -9.10411 | -48.80319 | 2026-10-10 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eed59c04-978a-39bf-a471-b7b9e18f5682 | -7.90178 | -54.71009 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7477246-9eee-3a7d-a91f-3a41dcccb215 | -7.23276 | -55.07711 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d3cdbfb-f839-33ba-ad09-393d8d6e4e23 | -7.03056 | -47.65213 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fb09e6f-a151-340d-913d-048823f648bb | -7.91444 | -54.71703 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b9323f-9d6a-380f-9e34-5dbb2780a620 | -9.87281 | -50.51871 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e93e86b9-8e42-3fbc-82d4-9eb6d247ee9e | -7.47583 | -55.7031 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f3412e3-130d-31b9-9eb5-095efaba490c | -5.97194 | -55.34415 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c1e524b-c9ce-3b9f-9798-30aa5620d654 | -11.56427 | -43.69022 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18246f5a-0e32-374a-ba7e-5622730eeddb | -14.01779 | -48.75965 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd098339-a149-3c72-b9c9-abc799770cd3 | -9.93984 | -44.88825 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0128351d-82bb-37b7-9d55-c4c2e38210a8 | -6.94514 | -59.10044 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b93caeab-5888-3f9c-aaea-4c0a750225de | -6.77515 | -48.6633 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b2546f7-1bed-3f65-b138-659ae3adb0ef | -7.92024 | -54.73685 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c48e417f-6fbd-30f0-8b8c-709b00448bea | -10.89884 | -44.82622 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 382a1c9f-935f-3d88-8765-35fc96270848 | -8.25953 | -46.4189 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc18933d-d3ad-31e1-bd83-5ee5850a1835 | -8.25667 | -46.41469 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54d09e8c-e123-35fe-b8b5-95395809ff53 | -11.96062 | -43.48436 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c75a39eb-a436-3abc-a991-d30e484ce168 | -6.48051 | -55.95498 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d77d11c-7ec4-3899-8481-61e9d025614b | -13.72728 | -49.12366 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a8b2bec-0659-3eca-b53d-5e6901a0513c | -9.92444 | -44.78476 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 559618d9-337a-3587-b34a-bcec1ad1d055 | -10.46595 | -47.33034 | 2026-10-10 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef5fd4cf-9ece-3f3f-9c49-fe2e3a450567 | -10.88836 | -44.79145 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3ec7baa-c2ef-3884-a09f-6d38dc8e6fab | -13.68951 | -49.12474 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README84.md)
