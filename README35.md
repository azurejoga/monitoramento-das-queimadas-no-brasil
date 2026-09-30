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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5caa36a-b2ad-3782-86e6-d28be5fe87b4 | -12.70754 | -46.96329 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f712ec3a-29c2-37a2-9709-8f6188b80830 | -13.33922 | -43.94994 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2509b74f-a63d-37aa-abc9-d6d77f05f3e9 | -11.37015 | -43.35736 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54dfb534-006c-3de7-b5ef-befefbad3291 | -13.36895 | -46.82664 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f78d296-c977-3ab4-82eb-d04f7adf2a10 | -12.26176 | -50.28331 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b94094-aede-3c3c-9a84-21c58a6bf16f | -14.13178 | -46.26613 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe43c875-dbd3-3e3e-9436-904d845e68a7 | -11.82129 | -46.89399 | 2026-09-30 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84cdb100-8393-3499-8c7a-31bf1ad7418c | -15.4492 | -46.14374 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7798d34a-9128-3531-9267-db74fc8c7f3f | -14.85563 | -48.18537 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e84bada-5584-3d41-acdb-b0afc4d6eef3 | -11.35238 | -50.97781 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebe760b8-6a3b-36a0-9740-e2f9f0f3ac30 | -11.96819 | -51.00777 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b07b18b-f74a-3a84-92aa-e66be47be382 | -10.82232 | -48.71719 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 897adf51-c6de-343b-a225-54eb88759dd8 | -13.07306 | -43.27527 | 2026-09-30 04:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e549f68f-a01b-3937-9ab5-5418112cda60 | -10.90259 | -43.86055 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ad053d1-c75f-3b43-9dc5-d31ac0a7da37 | -11.98523 | -50.88535 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38781cf7-3c31-34d1-a67a-1ac443677a7e | -16.01885 | -43.69173 | 2026-09-30 04:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96d27151-2895-3f45-8396-179a8bd11282 | -13.64301 | -45.5639 | 2026-09-30 04:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebdbc2ef-b8f9-326b-a55a-2bb21ab1691a | -11.38314 | -43.46661 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a3f19dd9-93ac-33cc-8dcd-5e3447cbf5f7 | -8.26472 | -54.75286 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb0047fa-f965-33b1-85c7-4cad8e1ea7ea | -16.4201 | -43.30369 | 2026-09-30 04:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a1174be-aee8-3708-848d-bdde1506adb8 | -11.43966 | -43.44735 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61879363-b128-3102-abe7-b54f0148b166 | -15.97457 | -48.1397 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b43479f9-3823-39c9-ba2b-af5424703e67 | -11.70269 | -43.44505 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf21fbf6-fc3b-38af-89d3-c68bb362c415 | -12.72752 | -46.98866 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1601165d-01b1-3a2f-ac03-4445d03c8036 | -10.89497 | -56.17308 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ede69992-60a6-3c51-ba56-5c85dc96f5a8 | -15.09075 | -48.32751 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f8564fd-949e-32c7-b687-641246d23e76 | -12.34352 | -48.19479 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a7d4cad-b465-3e99-a59c-2caa53c2cc7c | -12.78766 | -54.00483 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efe93eb4-dea1-3841-89a9-371957e94248 | -10.88697 | -43.62262 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 440581c1-288e-3f39-b3ae-43f2233a5635 | -12.08165 | -46.47523 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 309010f6-de7d-3cce-adfb-66d5e723f361 | -10.76256 | -52.13079 | 2026-09-30 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bfdf9b9-499c-3285-97c7-fae11a07e6f0 | -11.37731 | -43.36137 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8bc73cd9-35b0-3b1d-9f58-35051cc10b80 | -10.90059 | -56.17546 | 2026-09-30 04:34:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05875730-c418-31e1-88d8-3bb3c6e992d6 | -10.7773 | -47.724 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cda4d33e-a413-3e48-97c9-b9b665a5fb37 | -10.52196 | -45.36082 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17e1ec40-da42-3a8f-9e27-af952db73664 | -10.90716 | -43.85357 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bd59949-3f58-32e1-973f-c7f1df0e6b26 | -15.75262 | -46.03659 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c54e1238-5c70-36b4-a15b-19ddffb7a33a | -10.57642 | -50.84972 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b295c51c-686c-3729-aa7d-175947a55a78 | -11.16659 | -44.77677 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ed3ca1e-529d-317a-b8d0-04741df85cdc | -13.30389 | -43.46733 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba0444ad-78b9-3d7e-b135-7952dcadc362 | -9.78574 | -44.81365 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af1606f3-a49d-349a-834c-a8c44a79a4df | -13.07245 | -43.2794 | 2026-09-30 04:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f5e12cd5-fe73-3e94-949f-735b5916ad63 | -13.33467 | -43.96068 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16dbecc5-34b6-3d76-89b4-f70e305c1150 | -11.39742 | -47.43465 | 2026-09-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04595bed-b4a1-358d-9e10-d9b3f47bfce1 | -12.01391 | -47.80626 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07df8c37-5897-3168-bcb0-ca79d0beb70f | -11.4046 | -50.99113 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 301de2ee-c7ba-3b9d-b37e-912de1d92fe6 | -11.84802 | -50.95643 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfb19fa-c31b-39a0-bd0f-54b6bf1f736b | -9.82235 | -48.21868 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f2b57fb-0b65-3b0b-8fed-d4730593e22f | -13.42797 | -43.81411 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| fd6e5ad1-1cc9-3d57-9358-a2b192186548 | -12.78666 | -54.01017 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc217303-976b-36da-b9d0-7b7c91b2d4ab | -12.60694 | -47.23655 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0606ab9-efbf-3233-b221-bcc534663b00 | -15.97855 | -48.13663 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ca96958-7422-3fd2-bbee-06c93b83740c | -12.23825 | -50.25913 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e79e63c5-df81-3c78-9d23-f43ff9e36cbb | -10.21709 | -44.64555 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c09fa35-831f-3f1d-a82b-5529a2cd7521 | -11.41515 | -43.4676 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afafe0a5-4d16-3a50-b725-75ff1b7e7f1b | -10.57705 | -50.84606 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24892507-8804-3101-a3fb-56284b99f2d8 | -11.96416 | -51.00702 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80d70dee-56e3-364c-9783-8315c26011f8 | -11.85018 | -50.96791 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09e946b4-f927-31d0-a734-cec19a86d819 | -11.1767 | -44.82243 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 62b7cd7c-9048-3430-8aa0-588da53a2dfa | -11.63562 | -43.53222 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c07ba2b2-7eef-3792-8b00-060ecd2d521f | -11.11963 | -45.91529 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cffa05f6-fdcf-35f6-aab0-f0e96dde9416 | -11.37673 | -43.36531 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 134b119d-b8d6-3c92-b32d-db5766c22f31 | -11.8115 | -43.31877 | 2026-09-30 04:34:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 129525ff-c3ab-312d-87f3-f9253466df6e | -15.12703 | -43.61999 | 2026-09-30 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 90433121-47ca-3a22-bdca-8b3af07b7b9f | -12.60357 | -47.23598 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dced5f9e-0233-343d-9636-b6c705309899 | -10.68349 | -50.29029 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 252227fc-110c-3f0a-b4d4-aa5007ffeaa7 | -12.88801 | -44.80544 | 2026-09-30 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d694685-91b8-3a01-a404-a5b8e18df35e | -12.07313 | -46.45224 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e8e8527-ab85-35a0-a34b-ea21c9fcb97f | -17.10452 | -46.47011 | 2026-09-30 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ce68843-bf47-3e43-9a77-d2ff59916f2f | -13.21847 | -48.55209 | 2026-09-30 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ff28565-5e76-3364-860f-87c1c08a7f85 | -13.35618 | -46.82086 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9161c19-ea5f-36af-b5e0-d302b987b205 | -11.4018 | -50.98312 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b2de9db-15a0-3204-8fba-29c488d03b38 | -13.30247 | -43.46991 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88e1bb1c-b4e6-3209-b252-5bd191df7c9a | -15.83661 | -42.55946 | 2026-09-30 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b8ada19a-cc2d-310f-afd3-a5ddb4cccf32 | -15.76211 | -46.04187 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a77e494d-07d8-3e81-be48-74fc2df00349 | -11.43735 | -43.43898 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d157d66c-89b2-34e6-973f-f2fa6e68e167 | -15.5715 | -47.89233 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b8179ab-870f-3ec8-8cdf-f0a1dd13b127 | -13.37877 | -44.02357 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcfeec16-342a-3662-b96a-83be996f41fd | -17.52044 | -43.70465 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa6a0679-dd43-312e-a034-5abff7a0d1ae | -8.94063 | -49.78049 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e0d7392-1248-3f2e-b2e5-9ead93ef81d9 | -15.7744 | -46.029 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ef82d5c-4479-39a7-845c-8c3c737a1d9f | -10.91116 | -43.85033 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 170c6fc5-aa04-3086-82c4-6aeaf4c8ba1e | -14.20387 | -42.07515 | 2026-09-30 04:34:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 16056943-d5f7-3146-bc05-8043a43d80a0 | -11.19803 | -45.12512 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 809d7246-afa1-3617-b531-996f1ac486e8 | -11.85701 | -50.97655 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 153f9004-f767-38dd-bab2-f476163ddfec | -11.98565 | -50.88689 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a2b1fba-4bba-3f3f-806a-0ee01dbd0a0f | -10.69877 | -44.43866 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ef7e7f2-a6b9-30fe-a5b6-fb57017c8f39 | -9.93505 | -50.15154 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 203eec12-f101-3561-a97f-ec7e098dc0f5 | -14.53362 | -48.29415 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c199ff51-3765-3999-bb4c-59e17ecd0e01 | -11.42513 | -43.42506 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdb9be06-9b9f-34ff-8bbf-bcacbb6cff4e | -11.18188 | -45.11892 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1162b605-2fea-301f-9462-fc6d9a9d9684 | -12.2391 | -50.25431 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5e5aa18-782d-3aaa-b778-8ff861ae9545 | -13.32699 | -43.95998 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73e40cb1-c3cf-36ca-881a-752e34bcd127 | -12.30297 | -47.95941 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc9efe4c-2f35-346b-8367-57ff35034518 | -9.1191 | -48.52205 | 2026-09-30 04:34:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335f3ff0-f0d6-3299-a707-ec9106ac7247 | -10.78639 | -48.75441 | 2026-09-30 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa268cc-bdc1-3ebf-8910-7fbef7137552 | -10.78408 | -47.25433 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb1b5b98-aa52-321f-867b-1f0df88e4db0 | -11.85992 | -50.98413 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 547ab84d-363f-3a6f-bf15-cb1b55c7fcac | -8.9463 | -49.78825 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3871f444-6ff3-36f4-a893-263a93f7ba11 | -11.70737 | -43.43772 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README36.md)
