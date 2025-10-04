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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6190238d-8447-317a-8653-9126ecd6a04a | -18.63214 | -50.67818 | 2025-10-04 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e5e8585-fae7-3b3e-842b-602f29588443 | -15.32409 | -56.94226 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38eee936-aba8-3a0f-8c35-b349b364454d | -17.29456 | -49.26785 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d25600d-be58-37ff-ae1d-cfe839153ae5 | -22.23959 | -47.60857 | 2025-10-04 04:17:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a752a71c-4386-3703-b2cb-706aa47f8b2e | -15.33108 | -56.93964 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14d67219-88bf-3768-97f2-d59a849bd52d | -19.61727 | -46.6936 | 2025-10-04 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ffbb345-e3d0-3360-886e-336b56dc22d6 | -19.69512 | -47.96573 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df862320-1f7d-3dbd-a968-e82d88d9e473 | -21.69952 | -50.0598 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55bbab60-80cb-3e43-8ce2-3d38061e67ea | -15.60004 | -52.48653 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b7dbdd76-c15b-3b32-a8f9-29d59ca818eb | -16.04675 | -43.70164 | 2025-10-04 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 120c74e2-a4c5-3b77-a2c8-5dbcca4c0050 | -16.35373 | -47.07248 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80996db6-4aee-3f20-9288-84391bda6f47 | -15.65294 | -46.25843 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18c76317-1a5b-30e1-9858-40ee4d1a5608 | -17.98771 | -51.63841 | 2025-10-04 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 833facf9-f168-3e5d-913c-72837342b994 | -19.68365 | -44.61213 | 2025-10-04 04:17:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4b95821-afb4-3a20-93be-74f6657c4def | -18.15938 | -46.10168 | 2025-10-04 04:17:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49ebb08f-5427-32c4-a745-de5b64e29eb8 | -19.73684 | -47.19014 | 2025-10-04 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27fd0fd5-215f-3c3d-a51b-54b1c18450b4 | -18.45937 | -49.4451 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9faa9b6f-7fe5-3e76-ad01-313995d8373e | -20.3887 | -44.46093 | 2025-10-04 04:17:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4f14d3f1-ad05-39da-bb28-a119721cec22 | -22.27529 | -46.75034 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf56c9d4-bbee-343b-8459-509ee125778a | -15.21214 | -56.83901 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14f0d5ff-ba8e-33e8-83f7-138a408f3e09 | -18.18723 | -43.55538 | 2025-10-04 04:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d03f1a9a-6016-387a-a627-fa33be6ee0c1 | -15.60172 | -52.49378 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4900936a-f35b-3756-82e4-0da534c5fc40 | -20.46758 | -44.82394 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f52a767a-461e-353a-935b-b0de1941bf25 | -14.95593 | -49.99451 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2161c97a-c01f-3a2c-a8b8-1ea92e19e7fa | -15.61656 | -46.94519 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c28b15c2-0742-38d5-9929-459be2d62fde | -17.55202 | -44.41952 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c093ec0b-a3d1-38b8-b10b-6772e29fbbff | -15.86934 | -46.26565 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da81937a-b40d-36e3-9d62-e03ac3f91949 | -20.13253 | -43.98739 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 344e52b6-d3b1-39c2-a9da-8bed30678e89 | -16.0901 | -51.06501 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 026d8109-afdb-3b3c-971e-8265928c4c11 | -16.02054 | -50.95084 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f18b0be-4b4e-37f0-a5cd-f2b51cf134ae | -19.89056 | -42.62865 | 2025-10-04 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b65d409c-31a7-3e91-9c88-9014cae7ef2e | -21.68627 | -50.07108 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b2d8182-47d5-380c-8b85-893cea12b6fe | -18.57888 | -53.44032 | 2025-10-04 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 174f4b40-f493-3fb7-9695-abc761e609a1 | -16.39481 | -52.16027 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddd50400-beca-3900-97a3-54cb61b70542 | -17.62114 | -44.46154 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4faaa9de-16ed-3a32-9475-e011e6a78d89 | -21.84763 | -41.36956 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| abe16c26-b39b-31ec-bbd7-c7aed79d7ee7 | -22.43446 | -46.88143 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ddfe47b-0d5f-36bf-90c6-8c1321a89e15 | -19.72322 | -47.16842 | 2025-10-04 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2765ce1f-229e-397c-862b-f084b3964e6d | -16.757 | -43.95911 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12c8aa4d-072d-3c46-9721-3809e27a5bc2 | -17.08143 | -46.23359 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 485c6134-be64-3efe-acdd-50522dd0611c | -21.69149 | -50.06283 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7558b268-54f3-3bda-b275-a55d1f6cc892 | -19.47266 | -44.76711 | 2025-10-04 04:17:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c4350de-aeda-3a7a-9c2c-b5d0f6ceec85 | -20.81292 | -47.05712 | 2025-10-04 04:17:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb48349-eacc-3fb0-9d31-b918dab100ca | -15.34426 | -47.82065 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9213dc68-e028-3b47-98c6-946531fcb085 | -19.73288 | -47.19328 | 2025-10-04 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd1cf1c8-8e0b-3fbb-9deb-52f07bb08dbf | -17.63064 | -44.44421 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15146670-c3d7-34a4-a3cd-b5c7f4fc6368 | -21.03967 | -55.74455 | 2025-10-04 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10d3ccb0-7ba4-37df-8b32-5e9e5c136fcb | -19.8152 | -46.06919 | 2025-10-04 04:17:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94d8f16a-5877-399c-b073-5fdc02260471 | -19.71113 | -44.12368 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68716209-e0c2-37b8-95ce-1c2dea463379 | -18.64385 | -50.68064 | 2025-10-04 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c27d6654-67cf-3895-a55e-cd4f9c0d6872 | -16.69279 | -48.89245 | 2025-10-04 04:17:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 85909725-6c90-3ddb-ae80-cc62e1054866 | -16.06446 | -50.89951 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c130663-cdf9-3d97-a21a-2f54695ec149 | -15.21718 | -56.84543 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca4fc512-caea-3c41-be26-7b7aaef06bb8 | -15.37593 | -47.95263 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 170d6b90-2430-3201-997d-1423afcf69ae | -17.14754 | -47.03088 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d52df406-4742-388e-bac3-2953ed83bcf6 | -16.01081 | -50.9255 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 223bf0ef-ca7a-37eb-a379-a43496ac373d | -16.0448 | -51.00565 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff0fa6dc-cf9b-349a-8b20-3b906994ed59 | -18.46019 | -49.4404 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc22f8a2-e9fc-34bf-8e5b-2905e3875552 | -16.35715 | -51.47632 | 2025-10-04 04:17:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5cf63d1-c60b-3219-b489-ed587b5488b3 | -16.86115 | -52.78529 | 2025-10-04 04:17:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc43022-2019-3f2e-b9fc-b364ac3c9efe | -17.7062 | -47.08996 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72eeab1e-7e2b-3e8e-a3bf-0a876ad3d505 | -15.46449 | -48.54721 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db3fac5b-2cac-3adf-92d4-171ed83696f5 | -16.34004 | -47.11301 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 647c735b-93a8-3d57-8e9d-2a8a50480f33 | -16.29473 | -45.24555 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd19a607-2e90-3fd1-bcdb-a744edb3a65c | -20.46871 | -44.81633 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 15cc7917-4b49-3edf-87ee-1d2d554836bc | -21.06306 | -43.44933 | 2025-10-04 04:17:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b4e5e89-f9f5-3ce4-b21f-e9457ef2a700 | -20.46815 | -44.82014 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 54ac7c00-25a7-3302-b574-e84e313e6758 | -19.68777 | -43.94627 | 2025-10-04 04:17:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d66e1e95-7439-3284-a506-034b359197a2 | -29.94981 | -51.61854 | 2025-10-04 04:19:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| bbb26b02-216d-3734-a104-a4acf8193609 | -12.0314 | -45.1901 | 2025-10-04 04:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 577beee0-98fb-3b6f-a455-212eef3372c3 | -15.3572 | -46.2939 | 2025-10-04 04:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6835dce2-8b31-396e-8e14-950d81931ac7 | -12.0507 | -45.1872 | 2025-10-04 04:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e382d079-0519-31b2-b9c6-1a459716b0ea | -14.6521 | -48.3188 | 2025-10-04 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bf68eb9f-d0dd-37ba-a480-ea916ba1ac4e | -11.9147 | -46.3726 | 2025-10-04 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 266d33e6-39ed-36da-aafe-ed2c62c6f5c8 | -14.672 | -48.2933 | 2025-10-04 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c6403c02-9aa2-3574-b2b3-5ba2a84b701a | -13.2938 | -47.5905 | 2025-10-04 04:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 45b911b3-27f7-3665-bcc4-8657dc47fe15 | -14.6526 | -48.2964 | 2025-10-04 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 72eacfa4-c54a-3553-90bb-f03a2e44f221 | -15.3376 | -46.2975 | 2025-10-04 04:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 185180d4-9425-3289-9f36-58a3ba1b4272 | -12.031 | -45.2132 | 2025-10-04 04:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 0c925eac-2683-3d12-bc23-da83c10749b7 | -6.8774 | -47.2334 | 2025-10-04 04:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ae50a3b3-af57-33ca-905a-c8af7ebdd237 | -11.9335 | -46.3926 | 2025-10-04 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 509c00e3-eb20-3ec4-b137-3fa871a4b2d3 | -11.9339 | -46.3699 | 2025-10-04 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b4f6d7c4-272d-30ce-985a-c9f87760e2d7 | -11.9143 | -46.3953 | 2025-10-04 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 4d543097-5d84-331d-8e4f-a06300a8fe16 | -2.25836 | -47.85799 | 2025-10-04 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e331d71-f3e5-3125-99f0-c88f4997d85f | 0.46564 | -60.43735 | 2025-10-04 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6838f51-b7fa-3efd-8e34-cffcf0593489 | 0.50624 | -50.77197 | 2025-10-04 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 332372bf-ffc7-3172-8f83-396b4dee9e86 | 0.50391 | -50.78114 | 2025-10-04 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8520e50f-4e1a-3b2f-85ab-c21552ac50ab | -2.25082 | -47.87647 | 2025-10-04 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff40cfee-62a2-3c55-8738-149308e5d9f9 | -1.78927 | -54.07641 | 2025-10-04 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 662d7430-facc-35ca-ae06-51ba2ce7463a | -2.68981 | -48.39389 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84ed9c2f-840c-396d-865e-b89a0329d3d0 | -1.88791 | -48.39536 | 2025-10-04 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa85190b-c711-34bc-8492-60aaa659fbaf | -3.45255 | -43.33575 | 2025-10-04 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54bf6006-b937-32d8-9d2e-75674dd35f92 | 1.03328 | -60.43301 | 2025-10-04 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 560b52ef-5232-3d83-9c3e-f69a582e4f9a | -2.25009 | -47.88129 | 2025-10-04 05:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91c056f6-18d4-35c5-8163-85b486d33ffc | -3.4391 | -43.339 | 2025-10-04 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad9d6963-a188-35d8-b2e5-90e6e3920226 | -2.68085 | -48.39249 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 612c1e5e-c22d-3c2c-975c-46a92b73d4ce | -2.68599 | -48.38876 | 2025-10-04 05:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39a18a79-2b72-3794-a51e-e027db64f870 | 0.50025 | -50.78171 | 2025-10-04 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0888e563-4c43-3ec6-95bb-5182220b0e23 | -2.59163 | -48.9299 | 2025-10-04 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c10d1e5-a1a8-35c9-8e39-b0b6416640bf | -3.45179 | -43.34101 | 2025-10-04 05:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README99.md)
