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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba673294-478a-3b39-af17-9bfdc0679b22 | -11.18429 | -48.61779 | 2025-06-25 03:47:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 016e696b-0e52-31cc-b4db-58bd121c1003 | -11.57933 | -44.64431 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70a20319-c646-314f-8dc3-92c69a6f0230 | -11.57115 | -47.43139 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16fafdfc-b981-3f03-be69-d04b959bc92c | -11.12103 | -46.97377 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0f1d7b5-da3f-3a6a-b65f-bbf6efcb7ab8 | -11.94076 | -48.42752 | 2025-06-25 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6fbed43-f6a4-3d6e-a054-48bb91f0abae | -10.44055 | -47.94958 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61bb8b90-e983-3019-b206-fc0f8a86fda2 | -11.94179 | -48.42248 | 2025-06-25 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f641f187-207b-321e-b3d6-50cffe5b8f8e | -12.80194 | -48.73672 | 2025-06-25 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4aef30b-3a97-38bf-95fb-9d75d06e930b | -23.33674 | -46.77462 | 2025-06-25 03:47:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d6b0366-814d-38f2-9c93-cf55b969d26c | -11.08401 | -46.64244 | 2025-06-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9896e31d-c350-36aa-8cd2-58e5cb2f5394 | -11.5928 | -47.61363 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c026ce16-760c-3074-801b-a3946e2d08b9 | -11.11343 | -44.52365 | 2025-06-25 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6eef2918-b51e-34fe-a54e-2bc413772e2e | -10.44686 | -47.95056 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1e21f21c-e088-3693-8799-ea7e387a5cd6 | -9.57477 | -49.11242 | 2025-06-25 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73120919-8999-3279-8343-b44b426f48f1 | -15.39987 | -43.20024 | 2025-06-25 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b1c3af2b-6ebb-3ef4-ad2d-4c3145cae6fc | -11.11169 | -46.9023 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abe79dd4-4342-3172-b72a-c195cfc28cc0 | -17.0823 | -45.94597 | 2025-06-25 03:47:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4c2e8c9-fefe-364e-ad30-70973df6c088 | -14.72203 | -48.4146 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 851dbbba-d0cc-3307-a18d-571d827feea9 | -16.08837 | -41.98329 | 2025-06-25 03:47:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae06fe3c-ef35-3653-92d5-9a1d4bac3ccf | -14.80248 | -48.29712 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae852d3-0693-3cf0-9e93-bed607899cfa | -15.9216 | -42.57789 | 2025-06-25 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9952c2fd-fc81-3217-8255-146db93ec4f2 | -16.39605 | -41.16886 | 2025-06-25 03:47:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bfaaabc3-b82f-365b-a540-294bdc215a40 | -13.61179 | -43.97717 | 2025-06-25 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6702ebcc-283d-3279-b862-41637a0256ed | -11.1268 | -46.9752 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ac3fcb2-4fc3-36c0-832d-7dd4b9b24191 | -9.81163 | -48.38956 | 2025-06-25 03:47:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a65b908b-27e6-392d-97d6-d9afebc9c5df | -15.92225 | -42.57434 | 2025-06-25 03:47:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8e774aa7-3245-360c-ad6c-0b699b32e953 | -15.4015 | -43.19813 | 2025-06-25 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2494054f-c81d-3249-bc49-9e2957f0790c | -13.05139 | -48.83289 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35fa2773-3770-3dda-98cb-970c13d87dfd | -14.71708 | -48.40853 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 560ff901-b5e7-3a24-858e-c74dc4f26541 | -11.77576 | -47.40233 | 2025-06-25 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5eab358d-9ef2-3cfb-aca6-4a47ed22f70a | -17.14526 | -44.72012 | 2025-06-25 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a4f1b59-03fc-3b86-9a33-b9babacf7d2e | -17.11241 | -41.57298 | 2025-06-25 03:47:00 | NPP-375D | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e42d8f3a-d062-3f03-bc7a-578b9f9cebe5 | -14.38076 | -50.32776 | 2025-06-25 03:47:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94104779-bfb8-3aef-837c-ae62d38d3b1a | -12.79565 | -48.73542 | 2025-06-25 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 70697b90-bc55-3751-8a2f-50ceca82ef7d | -12.51266 | -47.4363 | 2025-06-25 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51377db8-0e15-3e26-8a03-97d851eff044 | -11.12139 | -46.97751 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fce6f74-a58b-3322-920e-e379dd44229c | -23.45461 | -46.73063 | 2025-06-25 03:47:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 563ad678-770f-3723-bd7b-90af911cdba9 | -11.57199 | -47.42707 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 528c8dfa-9e41-3375-ab91-28c6ed77cef2 | -11.95596 | -47.01595 | 2025-06-25 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a04b14-e3d3-3323-b1b7-a0687014d056 | -13.04616 | -48.82642 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e87c719-51b9-3a73-840b-7f6b4972347e | -13.04507 | -48.83162 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8be54db4-3ee4-3827-888c-eba091a96558 | -11.95346 | -47.02828 | 2025-06-25 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb7462ed-0255-3b7b-85b0-28a6bc75bc6a | -9.56673 | -49.11734 | 2025-06-25 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a0a3a85a-524e-32e2-8e6c-0085a6cfdbce | -13.05248 | -48.82763 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7839bf5e-8be8-343c-99a7-df1c5957ff58 | -12.75428 | -44.41397 | 2025-06-25 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a178d3f-8ecf-31e8-a3c2-7af31072bd5d | -14.56726 | -42.94598 | 2025-06-25 03:47:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c6cf467-a00a-3c4d-9f48-19aad196db0a | -15.83073 | -41.82873 | 2025-06-25 03:47:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b376396-8b97-345c-a915-696670e1b6fc | -10.5994 | -49.47018 | 2025-06-25 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab6523af-ccc6-3d61-a8f1-83b32b9a7fc5 | -10.43954 | -47.9547 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c87d6903-e04d-3d4b-9c06-96f74508e271 | -11.57289 | -47.43318 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e41eb6d4-c601-3449-a128-860b482180ed | -11.61331 | -46.5009 | 2025-06-25 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5c95a13-f0b1-32f7-ab1e-eb9e44b5b628 | -9.57352 | -49.11871 | 2025-06-25 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1274a63a-7be5-3eec-9232-5c4e4805c9ed | -20.92936 | -49.09595 | 2025-06-25 03:47:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f8485df8-c360-3c1a-9f87-0f1f4b417438 | -10.94921 | -47.3881 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f30faa1-2c0f-3978-a5a2-bdacb84d05b0 | -11.57032 | -47.43566 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0feaab03-9025-3538-ab3d-dcbc405c9d06 | -14.37936 | -50.33403 | 2025-06-25 03:47:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36a68193-e98a-3f27-8c08-791f5b62f3c7 | -17.07627 | -45.95055 | 2025-06-25 03:47:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c07e184-eb69-3651-896e-a1431bec92e9 | -13.01413 | -44.10204 | 2025-06-25 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d7b97ac-28de-3ff7-ad1e-de565c28d481 | -11.12296 | -46.96928 | 2025-06-25 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49618d61-10a5-3b2b-991f-19061f07c7e5 | -13.03985 | -48.82514 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc17c23c-6563-37fe-b928-71f61de6bb58 | -10.44583 | -47.95576 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1b43324a-0e49-3ac8-acff-7a6c277b1e41 | -10.60072 | -49.46382 | 2025-06-25 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35e0ae90-0e4b-3d02-90e8-85f2c0191929 | -10.59954 | -49.46608 | 2025-06-25 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b05ef06-9fcb-357a-b816-83ad107c9cd6 | -10.4521 | -47.95694 | 2025-06-25 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a884cad7-3e78-3716-b5d2-7eda699bcd1a | -15.39232 | -43.20051 | 2025-06-25 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02d7fd27-6081-35e3-99ef-a4a9e8bd83b3 | -15.39581 | -43.20539 | 2025-06-25 03:47:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d394984b-73b7-3c88-a6a6-6d1bbb41b583 | -11.95263 | -47.03239 | 2025-06-25 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3681113-263d-390c-8605-c2fd7b8171b2 | -11.58006 | -44.64123 | 2025-06-25 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 951ab73e-630f-3d3f-ba12-b31b7296a069 | -14.35029 | -40.90703 | 2025-06-25 03:47:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b39ccef9-85a1-3c4e-b84c-449c71c5d95a | -13.60721 | -43.97626 | 2025-06-25 03:47:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e301c68d-89f7-33ff-a3bd-fb569d88a9d5 | -11.08419 | -46.64477 | 2025-06-25 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 824d1478-b846-36e6-97b7-b6da28176d85 | -13.04398 | -48.83687 | 2025-06-25 03:47:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 06287223-abb0-3709-88e0-f216bd3ba714 | -11.58773 | -47.60767 | 2025-06-25 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 815ff620-764e-3b85-9ea6-f3433295ddb1 | -12.80379 | -48.73788 | 2025-06-25 03:47:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3f60741-127d-3a7b-866d-a7109a121fdf | -14.71451 | -48.41059 | 2025-06-25 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e4dc866-8c7c-36ef-81a4-5b1ec7c8acde | -25.19322 | -49.32816 | 2025-06-25 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 707a164e-86cd-3034-a367-86cb1a138c04 | -18.72558 | -47.42227 | 2025-06-25 03:49:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c740486-1f0b-3f15-98ba-07880976e190 | -27.8287 | -50.30474 | 2025-06-25 03:49:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9703d896-f3e7-322b-bf37-57b7504f681e | -19.64011 | -45.19122 | 2025-06-25 03:49:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caba91e2-ec9d-3771-a9ae-8085ae173061 | -28.58876 | -49.43967 | 2025-06-25 03:49:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c519f433-0d20-3515-ba85-9638ff9b92c1 | -20.31098 | -44.51875 | 2025-06-25 03:49:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b12a2d69-0e18-38d4-8343-4ab56fe11644 | -23.98652 | -48.91846 | 2025-06-25 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebdc7fc2-ebe3-32f8-88db-d19e56511e22 | -4.5429 | -48.0151 | 2025-06-25 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| a2481848-a363-3ce8-bb94-2dbc8900eef5 | -10.443 | -47.945 | 2025-06-25 03:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a2102aff-9a7d-3b48-b1aa-854d861114ee | -6.1791 | -48.0712 | 2025-06-25 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c6fd3072-2dbc-3923-8c6b-cc5e57b35ec2 | -10.443 | -47.945 | 2025-06-25 04:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 74cffaf9-316b-3dc8-be23-91e85857b4a4 | -6.1791 | -48.0712 | 2025-06-25 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6ed954b7-3734-3582-90e4-5bc993efd15a | -4.5429 | -48.0151 | 2025-06-25 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 23264c67-bcb5-3a5b-a504-260a746c4936 | -7.09762 | -49.17812 | 2025-06-25 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63b6796d-d0bc-354f-80b2-6688a5f8cf39 | -7.01132 | -44.55843 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bcdc8424-4abd-3e31-8b07-696d05d80085 | -5.44118 | -46.28635 | 2025-06-25 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffafb326-c60c-38ff-899f-61b1e280ee8a | -5.73331 | -43.49876 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a32909a6-e691-393b-ab11-f8d2c73e69ca | -2.44821 | -47.50319 | 2025-06-25 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebb818d-c032-3dd3-ac0e-b84f0c5a9373 | -7.02488 | -44.56464 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 968ba039-51b7-3327-ab4a-46878c41136f | -6.17474 | -48.06684 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 127e4e89-a42b-3290-91b3-0049994a69ed | -6.90992 | -43.963 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 712e916a-b312-345a-a048-c4a6c440b5d7 | -7.03252 | -44.09729 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ca544e-c086-3aeb-b5a9-1fbcbe9de06e | -7.02134 | -44.564 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8abe8b06-b080-31ba-9ade-3b33e5ef7234 | -7.00842 | -44.55388 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd6cbb73-38a9-3e76-94c4-b8bce41f1b1e | -4.20081 | -42.81872 | 2025-06-25 04:06:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
