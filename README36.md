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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f44df6a6-f027-3994-9737-3f2adf604adc | -15.54133 | -46.81034 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2eb2b88-77dc-3260-a14b-61dcbe430912 | -14.67418 | -48.37245 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0ca5e7c2-2c87-3e25-a7a2-aab5594d52d3 | -15.54897 | -46.83758 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b793c87-5107-36c1-8fec-a1b93db36632 | -20.74033 | -44.3318 | 2025-10-05 03:36:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1ab1e900-8397-3c49-ae0e-ae28bd6e30e6 | -14.66943 | -48.2845 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2b0c8a3-de19-3898-bcfb-911dbc52eafb | -14.667 | -48.37111 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3a9a8e6b-9c30-351d-beb1-4945a2316b6d | -16.36075 | -47.06111 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a17a1d5-b78d-36c1-81d4-82ba5ee23aec | -15.50311 | -46.86203 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38e1aaae-6868-3f3f-bf6a-7cc242b2fc52 | -15.12716 | -45.74813 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f182126f-46f6-36dd-acb4-4b0440114315 | -15.54046 | -46.81359 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49298603-a1d8-3197-9cc4-33b16fc2dd7b | -14.67794 | -48.34715 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f7cffb46-61ee-34da-81d8-7883c9ddc6ed | -15.52749 | -46.87194 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7253e2c1-eac9-36d0-9ead-546d34e8462a | -19.95311 | -44.39953 | 2025-10-05 03:36:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a1497dd-436a-3ed5-874a-e741d5e7a9a5 | -15.5202 | -46.87694 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 083bc9f1-ecd5-3a43-ac01-22b5e94f675e | -14.6658 | -48.3683 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| eed71496-8df0-3f9c-96db-0c1f39985a6a | -14.68334 | -48.35656 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9a24b446-7f6d-3676-aa62-2b69d77744d2 | -15.30098 | -46.31354 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c21e74e-c171-3b69-a673-24b19cee68bc | -13.91105 | -48.19078 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20cd5bcd-57f5-3524-a317-bb503aa12253 | -15.1208 | -45.75024 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d759415a-3bdb-3a9a-be98-cd8cb8425ead | -19.63256 | -45.97382 | 2025-10-05 03:36:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d6e1b45-0ea3-3d1f-9d82-3964708d9ff2 | -14.79878 | -44.89947 | 2025-10-05 03:36:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7da510b1-99ac-358f-a897-f4328188a999 | -19.82141 | -46.07284 | 2025-10-05 03:36:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57b2a311-c5e0-3f0f-80c7-6977f7185af0 | -18.32713 | -45.88485 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 260b3c95-6e82-358f-bfd4-82bb0a252bd9 | -15.34329 | -47.33852 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d03ffd77-4ba1-345d-a4f4-9dea108f6dc2 | -15.32122 | -46.37154 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4847cbbc-947b-366f-9fb0-2aaab3dfcfc0 | -14.33089 | -47.67904 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 22ac2560-4fe1-3621-b712-b0ab52e82e59 | -14.87992 | -48.26639 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 32f6ae6b-bd7e-37b3-9375-f670fa97dd45 | -21.82759 | -47.40406 | 2025-10-05 03:38:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 08554057-f5c4-3289-956d-8fd8ed292f60 | -23.1904 | -45.62295 | 2025-10-05 03:38:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa9ae547-0a64-30cb-b626-52023e37a708 | -21.82876 | -47.39902 | 2025-10-05 03:38:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bb5e5392-2f20-3ddc-af2e-a9baab8f335e | -22.75564 | -42.01799 | 2025-10-05 03:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a05879c-9393-3129-850a-ec0978deebec | -21.82414 | -47.39206 | 2025-10-05 03:38:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d41e4b40-f851-3548-b729-7896081b2c36 | -21.07283 | -44.67735 | 2025-10-05 03:38:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e01066c-b278-37ca-9a11-3ff9f8a34a6e | -21.68813 | -48.42365 | 2025-10-05 03:38:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdf0808a-c8ed-3e62-99fc-7db5b42c98b7 | -23.01917 | -46.25179 | 2025-10-05 03:38:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 30b5b97f-528e-395b-9a3d-9cd62181b76e | -23.189 | -45.62923 | 2025-10-05 03:38:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0900a45b-2f7f-31a5-a43e-bd09150f7189 | -21.17534 | -44.28402 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 64c3a29f-7ebe-3aaa-b93a-0686bdeefbb0 | -23.69985 | -46.56401 | 2025-10-05 03:38:00 | NPP-375D | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ee34265-288f-3a48-9d09-92dd621b5154 | -21.16737 | -44.27629 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4361a7fb-347e-39de-8480-d60537a7e3b7 | -23.18529 | -45.62141 | 2025-10-05 03:38:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 080531dc-0916-3fe9-a885-b2d2a390ec73 | -22.48287 | -46.81882 | 2025-10-05 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c471fdc-5c34-37f4-81a5-6ce09f954367 | -23.44145 | -45.47715 | 2025-10-05 03:38:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b928ca1-e1cf-3e81-8f11-547c7c0ecf68 | -21.16794 | -44.26999 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e5bf7f0f-27be-35d0-a60c-39a8a0157aef | -20.88392 | -45.7686 | 2025-10-05 03:38:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be5b9d86-aa42-36e0-a55a-2ac12caab027 | -21.17611 | -44.28429 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4a58def7-4634-325b-b710-9ffe4e79035e | -22.99201 | -50.37255 | 2025-10-05 03:38:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a9e2bb80-50e3-3db9-84e5-c771e148f4aa | -22.48378 | -46.81489 | 2025-10-05 03:38:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7132b86c-7342-3b95-af3a-4b02a0bb25ae | -22.75482 | -42.02211 | 2025-10-05 03:38:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ba68a84-e7a5-34b2-99e5-b7f698221a53 | -23.44219 | -45.47382 | 2025-10-05 03:38:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 985d2446-3255-332e-934c-f13c364b88de | -21.16664 | -44.27604 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1fd09eaf-18c4-3b8a-b79f-8fbfde0e72cb | -20.88298 | -45.77286 | 2025-10-05 03:38:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d159b139-316b-3991-9b69-1f4bb13be4bd | -23.02021 | -46.25161 | 2025-10-05 03:38:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 662a0bd5-6c7f-3456-a31e-781a6215ed9e | -23.18971 | -45.62602 | 2025-10-05 03:38:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbcdd463-66ba-30db-acd4-7bc608e6bbab | -23.01476 | -46.25054 | 2025-10-05 03:38:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46942c3a-fe11-385b-8add-27edafb1c4f8 | -21.16863 | -44.27022 | 2025-10-05 03:38:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a271988e-81a8-3a5c-b783-2b086f0e692d | -21.07433 | -44.67729 | 2025-10-05 03:38:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b2f7a99-e35d-3ea5-a185-4eb150f0cdb5 | -11.8418 | -45.0799 | 2025-10-05 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9c08b813-7e41-35a5-8c2b-34f14bd34cfc | -5.8374 | -44.4399 | 2025-10-05 03:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2623c45a-86d2-308e-af1f-684a5013310c | -6.4134 | -43.0489 | 2025-10-05 03:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2afcbbb6-14be-302e-8bef-aaaedebd0a18 | -5.795 | -42.9358 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 353.9 |
| d3b52f64-a2a0-3426-9e18-bc4c82a62845 | -4.6318 | -43.1816 | 2025-10-05 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7165fadb-d1f4-3ddc-a7f5-1448a2304856 | -10.949 | -47.1082 | 2025-10-05 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 4ad7363b-12bd-3f9d-b6dc-c81795293d40 | -8.5956 | -46.2798 | 2025-10-05 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 063038fa-7e7c-3718-8ad9-7f2b08d878d9 | -13.1161 | -43.847 | 2025-10-05 03:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7c600c1d-977a-3021-8836-df9ef902c9f1 | -18.3345 | -45.8734 | 2025-10-05 03:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2eaff10e-6e97-3421-bd58-5fe1e5d5a8e9 | -13.2745 | -47.5933 | 2025-10-05 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 87d2d478-87f8-317e-95b7-6ea398e9a80e | -14.3353 | -47.6755 | 2025-10-05 03:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 54bfb65b-0d78-3492-b14b-b3fd838e3b62 | -5.776 | -42.9607 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 104b3baf-16f5-3cc4-afea-95f3e44ed334 | -4.6505 | -43.1805 | 2025-10-05 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 858a6436-4b72-3e0c-82c6-ed596d8eb86c | -13.2741 | -47.6158 | 2025-10-05 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0363c4c4-9737-3a84-b03a-a56dd84c52ed | -10.9497 | -47.0634 | 2025-10-05 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2ab27f2f-78a7-3b6c-8ac0-d593cc56942d | -14.6707 | -48.3605 | 2025-10-05 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 601def9a-afa7-337d-a328-5ef3fa3859bf | -6.1538 | -44.6446 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 31763897-2881-37a8-84de-bafbfe956c63 | -4.4445 | -43.2397 | 2025-10-05 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9036215f-294b-3fc5-b4e2-53edcb1683c5 | -5.7762 | -42.9372 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 329.8 |
| 3b4ca6dc-0e47-31cd-afa8-06bb6b37e4c5 | -10.9494 | -47.0858 | 2025-10-05 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 81fbcd29-d46f-3263-aa15-d1c4bb8c0d97 | -8.5581 | -46.2611 | 2025-10-05 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f1643859-7ff4-3c6a-9a86-41ee5acc87e7 | -5.7764 | -42.9137 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 4e94392a-2a7d-3737-acaf-e69537556bbd | -18.3338 | -45.8971 | 2025-10-05 03:40:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4e15f757-b70c-31a9-b143-99d78a1982ad | -10.841 | -47.9644 | 2025-10-05 03:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| bc17e976-25e9-3d54-be7e-2f3755b24c9a | -6.1534 | -44.6903 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ab35ac25-e643-3bae-9353-3515cff98f5c | -14.3348 | -47.6981 | 2025-10-05 03:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 08dd9390-65d0-362a-9676-5e241da26c86 | -19.0155 | -50.6045 | 2025-10-05 03:40:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 06717fd9-e1d3-3133-8b22-5c91c5addf63 | -4.6317 | -43.205 | 2025-10-05 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e1d49849-8bea-3ff0-a4e7-31482efafb82 | -6.1351 | -44.6461 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| cb5478a4-3f0a-3740-8c35-af506a2cb91a | -6.1536 | -44.6675 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 357.9 |
| eb14360d-f169-3778-ba73-f37aa6cc3073 | -12.9844 | -51.0433 | 2025-10-05 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8e5fd61e-ff17-38f2-b384-8de2f2483f88 | -6.1349 | -44.6689 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d750d07b-d468-347a-b3ab-40749ed8f7f0 | -15.6015 | -52.5102 | 2025-10-05 03:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 1c5d17b9-968b-3699-883b-b93bdd8f8267 | -5.7952 | -42.9123 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| ccc8853e-ad2b-3286-92a5-dd3693651339 | -6.1723 | -44.666 | 2025-10-05 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| eb052370-aef5-3990-bea8-4c1bf3955977 | -4.6504 | -43.2038 | 2025-10-05 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 48d17c55-4506-3e03-a3a1-08e26b86bb45 | -13.2934 | -47.6129 | 2025-10-05 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 87f4cdb9-c666-3b04-bb98-93308e4dffcc | -10.9303 | -47.0882 | 2025-10-05 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ce234121-d941-33b9-82d1-b76373b21e22 | -5.8891 | -42.9048 | 2025-10-05 03:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 89d1dde7-bc74-3d82-9ee4-29c00bdd85a5 | -9.2973 | -46.0026 | 2025-10-05 03:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4b34f4fb-49dc-3762-88a0-507edc7a8a16 | -8.5953 | -46.3022 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 56ead8f0-ab94-34a3-8b9b-a20105c1ebb9 | -14.3353 | -47.6755 | 2025-10-05 03:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 64c2a8d2-d03e-3a0a-b76a-c741d42868ba | -10.841 | -47.9644 | 2025-10-05 03:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 330720ca-0efb-3c45-9480-36b35ff1ba27 | -6.1723 | -44.666 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |


[Clique aqui para ver as próximas entradas](README37.md)
