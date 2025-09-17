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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75b62b08-9fa7-30cf-8dce-45b680bd2de5 | -15.42076 | -46.15672 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a643a04-660a-3c39-9c27-70e13c618649 | -14.60469 | -49.36875 | 2025-09-17 04:12:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43eec149-e41e-32f0-83f5-10c2da17de23 | -12.28099 | -43.83002 | 2025-09-17 04:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1807c244-53d2-3c63-b463-14299f8601c9 | -15.42946 | -47.32534 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae7d19d2-fa98-3f1c-a0db-55ce7668e9dc | -11.60204 | -49.81759 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c83c413e-d346-3ed1-85f8-ada4159c2034 | -15.98565 | -46.45024 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54bbe51f-ca85-35fa-94f9-9845c6588230 | -12.06546 | -46.56368 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da19c2e6-5b6c-3415-bb6d-503410885849 | -12.72444 | -48.00368 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67d559f7-71a6-3155-ad78-9b5c833d5bee | -16.42449 | -45.66724 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4071301-e713-318f-9463-e3ad8dd82f03 | -13.16367 | -43.32748 | 2025-09-17 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64f79c76-3954-34f1-aee4-21ece71fce35 | -14.61988 | -46.38963 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 469e22ad-9481-394e-986b-dc271f9e7bf9 | -12.60722 | -47.9822 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c16fe85-3b14-3382-bd6f-5ef50be1bf63 | -15.40196 | -46.14169 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e61b728-61f8-37e6-a3b5-8bc817da2801 | -14.6005 | -46.39519 | 2025-09-17 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881c192e-3cae-3584-89c8-3a92c8ae798e | -14.39539 | -43.53372 | 2025-09-17 04:12:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 215b415d-8e21-31f3-96b4-b4eb6634002b | -13.22749 | -47.29581 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79564dfc-8611-341f-8f2f-8d24fdc2b557 | -18.32957 | -43.29158 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 619ec69a-c97f-3b6b-81b3-702eea1f72bf | -17.33351 | -46.79288 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37522f9e-9bc9-36bf-8891-86f0d2314ea1 | -18.54564 | -48.14731 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e464568-b7b7-3a7a-affa-fa150ec7b1e7 | -17.96194 | -45.24632 | 2025-09-17 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e18e28c-45d3-37d3-828d-73895bcea0ee | -17.72158 | -43.56292 | 2025-09-17 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b80369-7951-3ae2-aebc-3e19c7225bd8 | -18.54313 | -48.14429 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d3222b8-5356-3354-ba97-16695a16b692 | -21.1432 | -46.96761 | 2025-09-17 04:14:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98dadf77-29e6-3aa3-84e5-13af1a5b3a94 | -21.42354 | -45.466 | 2025-09-17 04:14:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c1bf322b-3278-3ddc-a35c-4b04ebdf3771 | -17.72102 | -43.56655 | 2025-09-17 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cf5517e-86e5-3f8f-aa2f-6d244c99f5dc | -18.16582 | -45.19091 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60206cd7-bec1-37a5-89c1-b75a575b82d0 | -18.52541 | -48.15314 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cd16ea4-df9a-3eef-91d6-d54f0c4762f5 | -18.32733 | -43.30627 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fc1afe1-32b5-3df4-b63d-9947051fbfb0 | -18.32453 | -43.30204 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 50bf6bd1-43c2-3272-84c7-7295afa9a8dd | -21.14663 | -46.96828 | 2025-09-17 04:14:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c1a276d-5956-3391-bd91-d003ed7b38ca | -18.53686 | -48.13177 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17935da7-5a08-326c-afdb-a015fa09af5e | -17.87498 | -39.83843 | 2025-09-17 04:14:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00d0f047-b64a-3065-bb5b-e1de21a6feca | -18.3697 | -43.33208 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 46445265-02e7-347b-9c14-cab0537fb93c | -19.55214 | -47.69397 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7829aa6a-a06c-38cc-b06f-76307f0faada | -19.55571 | -47.69472 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6896d8e-c78e-3154-8dab-236f15a88573 | -18.33459 | -43.30376 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2c149d6-6c9b-39b1-a2d9-5e44169920e3 | -18.83628 | -46.75202 | 2025-09-17 04:14:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 954f7f1f-333c-33e2-824e-1565c1ba181b | -17.56064 | -43.79286 | 2025-09-17 04:14:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47162bbd-096f-3191-b3b2-3cdd1587d2b7 | -18.36858 | -43.31678 | 2025-09-17 04:14:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d05ead0-4fa8-39e3-8bd2-3b116c1bfd1d | -18.5225 | -48.1479 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e82439fd-752f-341c-bd5c-465bf0c5d9ae | -18.33236 | -43.29586 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ab66210-9a54-3f84-a30c-69d9f5d0e0a6 | -18.31838 | -43.29723 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 38eac296-4b3c-3442-839e-568b0d803bd4 | -18.17433 | -45.18093 | 2025-09-17 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 812a82e2-a634-30ff-a11b-49f4bc2383d6 | -18.36471 | -43.33174 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85730aa4-4cbd-33b4-b933-04157cb5aeb9 | -18.32509 | -43.29837 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28e35048-6910-381d-ba29-c912068c7fe3 | -21.5694 | -50.1181 | 2025-09-17 04:14:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| c686e297-9675-344c-8f2b-5113106295fc | -17.32926 | -46.79644 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5ec974b-3412-31e3-86b2-ae3bec192e0d | -21.56838 | -50.12346 | 2025-09-17 04:14:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| 38d06b9e-7b97-3f77-9b5a-9a8ac3da2568 | -16.98973 | -45.86023 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f36c5d2-ddfb-36cb-8b7d-ea9fc8a3574a | -21.6046 | -50.3252 | 2025-09-17 04:14:00 | NPP-375D | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 30398fed-6276-3459-9ba9-e4248f29b4df | -18.67409 | -43.25086 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c6a3afb5-acbe-39d2-93b1-c27e8396ad05 | -18.55445 | -49.24856 | 2025-09-17 04:14:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 89ad99b5-c5a4-3b8f-8658-ce5e2e9611e7 | -18.61662 | -43.62551 | 2025-09-17 04:14:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03b58bda-d043-3e03-8df2-ba8de8df7a46 | -19.73783 | -47.7675 | 2025-09-17 04:14:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed649d98-3f94-32ec-a370-12c1c1921b13 | -18.32901 | -43.29528 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac974fc7-9327-30ab-abd5-8c4c2deca0ef | -17.71721 | -47.94241 | 2025-09-17 04:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be24428b-68fa-3e4e-bd3e-60d0430b384e | -21.56443 | -50.12263 | 2025-09-17 04:14:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| 901fa970-7f19-3167-aa27-0f8fab8dc014 | -17.33707 | -46.79344 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94acb094-78aa-3c56-9dfc-569becd98f16 | -18.46064 | -43.25507 | 2025-09-17 04:14:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 35fb1866-318c-305b-a7fd-a15824c44ffa | -18.32342 | -43.30935 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f2a255c-3cca-3454-b42f-599e96e51aaa | -20.40428 | -40.61164 | 2025-09-17 04:14:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec747d63-b045-3a4d-9740-5b9f0226ab3f | -19.55496 | -47.69905 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4aa5d103-7f0b-32fa-b32e-211eaf629b44 | -17.04414 | -45.89397 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 419c0dbd-7e76-3fd2-a5b0-21ed21e5d23b | -17.19574 | -45.9191 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc18322a-a415-3422-be08-fd30657ad1a7 | -18.54105 | -48.13459 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c82147-3bbb-3630-8786-57205967768f | -23.50808 | -47.05091 | 2025-09-17 04:14:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1a46ad39-85dc-39fb-90f4-1413354ab8c7 | -18.33571 | -43.29644 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7e75d954-19dd-3043-a93a-a3a9bb2873af | -18.24686 | -43.62894 | 2025-09-17 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75023420-db03-3bce-9dc3-518e22147de8 | -18.19231 | -44.53593 | 2025-09-17 04:14:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 51923688-464b-364d-9282-0822678b9d01 | -19.55289 | -47.68966 | 2025-09-17 04:14:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7b3f5a6-9418-3734-b32e-fbe1e9f81e85 | -16.8874 | -45.78695 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eb9fbcd-6834-3c03-88b3-f9df63a3ec38 | -17.72492 | -43.56348 | 2025-09-17 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b02bf7a-8edb-3621-a629-273274cd9dfd | -18.49626 | -42.69685 | 2025-09-17 04:14:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99968e41-d3f6-304d-abce-06f43fc1ffdb | -18.33124 | -43.30318 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc1f0d31-1133-3357-b6c7-30eafeed9ec3 | -23.50802 | -47.05214 | 2025-09-17 04:14:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 521553bb-2a87-3f4e-b9d5-ddbe1d8c3768 | -17.95798 | -45.24939 | 2025-09-17 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fca922a-aed9-3fcb-9f54-c19b86763018 | -17.70891 | -44.7591 | 2025-09-17 04:14:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ec301d-e603-3d79-8015-2f4522a71591 | -23.45426 | -49.25172 | 2025-09-17 04:14:00 | NPP-375D | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50ad79f8-20f8-3352-ad04-d04d11b390e1 | -20.42883 | -40.74587 | 2025-09-17 04:14:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1b1f45e-5d50-3dad-b810-f941e68eea9c | -19.07828 | -46.6462 | 2025-09-17 04:14:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 755b7394-0e3b-33bb-8f3d-c1e183031426 | -17.11493 | -43.59387 | 2025-09-17 04:14:00 | NPP-375D | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37839aeb-7201-3508-bf1e-f02e4225ed16 | -18.33068 | -43.30684 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e4934a09-bf81-3e75-a423-a3fd43712a57 | -18.37025 | -43.32846 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 32f9778a-697a-302d-88d4-972a69d476f5 | -18.33403 | -43.30742 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 447b3451-d87f-3692-aa61-0fd117cbcf3e | -17.19913 | -45.91087 | 2025-09-17 04:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a26b6629-6860-3f06-823d-f3b72e89c538 | -16.88525 | -45.77865 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce5bae9-279c-3481-bfcd-4a4704dbcec5 | -17.00066 | -45.85825 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81c5313b-853a-3fcb-bda8-9ab65fefc531 | -22.39754 | -47.14858 | 2025-09-17 04:14:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 90ef4abd-d489-39de-84c3-9d8331db6189 | -18.32677 | -43.30991 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| af724cf9-ae5d-35ed-9c69-5bb2346d2f5d | -17.32572 | -46.81708 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81561ea3-3e79-365f-9e8f-5a306dca3656 | -17.33564 | -46.80179 | 2025-09-17 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f448b4a-7f62-30d9-a924-232b4062f8ec | -18.32621 | -43.31356 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78e1781d-99af-3094-aeec-34a6edbdb5ba | -21.5634 | -50.12802 | 2025-09-17 04:14:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 739ed257-3980-31f9-8705-4ec28f67e40b | -18.32397 | -43.30571 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5985e078-f23f-3059-bf4e-b6bfdb8ab441 | -23.4232 | -47.16138 | 2025-09-17 04:14:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 151a13cb-a417-3fd3-ae12-801671edfe24 | -18.52168 | -48.15254 | 2025-09-17 04:14:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec0a4cb-b7a8-3ce5-be89-3bd9880068d9 | -18.33348 | -43.31109 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 59c9a282-4052-3eeb-a355-b65d8fef65ee | -17.23737 | -43.43493 | 2025-09-17 04:14:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a20ee3cf-69dc-30e9-83fc-c9919d42a9ae | -18.31726 | -43.30457 | 2025-09-17 04:14:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b84b2db-1762-3da2-b39a-ebab5317213a | -16.88953 | -45.79118 | 2025-09-17 04:14:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
