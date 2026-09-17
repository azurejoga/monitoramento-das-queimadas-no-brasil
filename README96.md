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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9850bdf3-2900-34ff-8631-68fb20de1213 | -8.4983 | -57.6271 | 2026-09-17 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 60d0a50d-7416-3437-97f2-7cf842db64cb | -6.6021 | -58.849 | 2026-09-17 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 7852f2cd-257b-3093-868f-0b3a44ff5cd2 | -7.1195 | -42.1548 | 2026-09-17 15:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 047a54ed-d225-3b8b-af10-854a23f8a9f3 | -12.7243 | -48.2734 | 2026-09-17 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 82229a05-5659-35e8-a34e-eb5a7a747bb8 | -4.5045 | -54.9646 | 2026-09-17 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 4d929a63-b969-31af-945a-4f275b3d1218 | -9.3577 | -50.0943 | 2026-09-17 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e6b4d902-ca26-3f29-b8f1-53b06dff2749 | -13.2082 | -47.0191 | 2026-09-17 15:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c4c63375-b5d6-37c7-879c-ac2dddbfeca4 | -13.3391 | -51.6176 | 2026-09-17 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c02bd0c3-5f8a-3297-ac1e-e1392753b2ab | -9.7608 | -60.4561 | 2026-09-17 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 46bf3d2a-65ac-3000-8c89-34c2a516fd36 | -7.8033 | -44.8651 | 2026-09-17 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1321c9a6-cdbd-35cb-9e5e-ba496df45db7 | -7.0428 | -59.2173 | 2026-09-17 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4a1788f9-3495-3de8-8267-3bc23c36104c | -18.8906 | -46.8284 | 2026-09-17 15:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 81674ffa-276c-33d7-8344-54923ea72458 | -13.3754 | -51.7406 | 2026-09-17 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a95fc02b-3961-30b8-82f8-72edbedb031e | -14.1547 | -45.1442 | 2026-09-17 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 216.3 |
| ed3a64b0-947d-314c-a0d7-c006b75c1ea9 | -11.8069 | -58.1759 | 2026-09-17 15:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fe97291a-b6b2-3368-89a2-419b2e8ec282 | -12.3766 | -48.4532 | 2026-09-17 15:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1ba2e7a8-237f-3a34-bc83-72487cbcf963 | -7.5143 | -50.9022 | 2026-09-17 15:00:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| df4e1a71-9978-38bb-83bc-066877132006 | -15.5397 | -53.8081 | 2026-09-17 15:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 891c5bd0-1ad5-308b-a210-cacde06c82a9 | -6.6515 | -43.6354 | 2026-09-17 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 993e06c5-6160-3e94-a4d4-0ce27ea245c7 | -11.2386 | -43.465 | 2026-09-17 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 73e0bf41-9184-3084-868e-cd924a7758e2 | -9.8322 | -48.3417 | 2026-09-17 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 325.3 |
| 09ddd21e-dcdb-3f4d-a1be-2fda7ec4959e | -4.5044 | -54.9845 | 2026-09-17 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 296.2 |
| fb4d2d26-b722-3203-ae5d-fb796443d611 | -10.8118 | -46.1594 | 2026-09-17 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 58abb877-eca8-369d-8377-be39a17bc7bf | -14.1737 | -45.1641 | 2026-09-17 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9300c768-7365-3427-8206-fc96ff2e04d9 | -3.4757 | -54.7171 | 2026-09-17 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| bd948778-da45-3a4d-94b3-beb2fa433874 | -9.3765 | -50.0925 | 2026-09-17 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b50ce08d-8463-397c-a575-86c23a27cd1b | -8.58 | -44.5552 | 2026-09-17 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| ce030ac4-977d-382c-a8a5-1b0b71446397 | -7.0242 | -59.2374 | 2026-09-17 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| fa9ddbdf-3a3c-35ec-9e7b-2cdb97f4d8c8 | -12.4537 | -50.7662 | 2026-09-17 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 2bdd883d-8d94-3b5e-b230-eb9e3baec2f5 | -11.3442 | -43.9906 | 2026-09-17 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| a7b4df1b-95dd-3840-ad8e-2844cd5be195 | -14.8183 | -59.5532 | 2026-09-17 15:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| dfedea35-d339-342b-9b61-ceafd5be1c6c | -11.3629 | -44.0112 | 2026-09-17 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 228.5 |
| bb18ebcb-36be-398f-a5a1-6aed57f9a9cf | -4.5229 | -54.9639 | 2026-09-17 15:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 9ed83312-eb1a-3083-930e-e0ee6077f06c | -8.8647 | -45.8693 | 2026-09-17 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 238ae85f-7307-370d-a636-f30fd8a0c1bc | -7.1384 | -42.1529 | 2026-09-17 15:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| d5b66af3-3f8e-30a5-833b-1494a93b40f9 | -15.5199 | -53.8317 | 2026-09-17 15:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| edac7277-507b-3b95-a66e-e66232666e43 | -10.3769 | -49.9723 | 2026-09-17 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| bf41678f-33b8-3ce8-ba96-c43b4b36cfbd | -11.3437 | -44.0141 | 2026-09-17 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 2e77c696-d0bf-389d-8b13-f50ed12b2b21 | -7.1086 | -43.1027 | 2026-09-17 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| b0fb896e-4187-3911-9e21-925dee1a6d58 | -9.3567 | -50.1796 | 2026-09-17 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 13e56e6c-2302-3939-827b-605a2b5b1cd4 | -10.642 | -46.068 | 2026-09-17 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 17f8de6a-8445-328c-8f60-34ef439d3646 | -9.7793 | -60.4744 | 2026-09-17 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 79053324-9d87-36b6-a657-01c44aa8fc23 | -9.4325 | -50.1299 | 2026-09-17 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| c30e2d73-6426-3e96-bcab-e0e7bbb40d8c | 3.9169 | -59.6641 | 2026-09-17 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 162d9035-5f20-3035-b0e7-41a0b1a33cb7 | -11.3446 | -43.9671 | 2026-09-17 15:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 06d8e5be-291d-331b-b87b-fe0936d4568e | -13.5719 | -51.4605 | 2026-09-17 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 568cfdba-6757-3bef-a37b-0d928ce8ead2 | -13.3758 | -51.7193 | 2026-09-17 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f147be04-5926-32b4-89fc-4948c01369bf | -8.8923 | -62.3917 | 2026-09-17 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5efec353-3849-39fe-859a-19643059af2c | -11.8928 | -50.0608 | 2026-09-17 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 36335db7-96bd-3e1c-8663-8a90d596d3f3 | -7.8221 | -44.8632 | 2026-09-17 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 26958d5d-6806-33e4-a570-7d042b0f83e1 | -6.0993 | -59.9076 | 2026-09-17 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 0f976d2e-11e2-32b4-b0f0-b269a6dcf16e | -14.1742 | -45.1407 | 2026-09-17 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 4f958e37-1128-331d-829a-08796aeb84bb | -8.4796 | -57.6478 | 2026-09-17 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| f90ebb45-b33c-3a07-bffb-6f39900bc568 | -9.769 | -46.0841 | 2026-09-17 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 194439ed-c31f-3f89-a34e-cfbcf127b67d | -13.3199 | -51.62 | 2026-09-17 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e03ae494-d3e7-34c5-a87e-ba122ab5ff70 | -8.8737 | -62.3925 | 2026-09-17 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1291ee43-b4a1-33ce-bc21-3ebfc82cdbc1 | -8.5239 | -44.5153 | 2026-09-17 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 89efd7d9-f939-3a0e-b31f-4a22717ab6e4 | -8.9108 | -62.391 | 2026-09-17 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d3031b70-f3b1-332a-83ad-1f64de3e5b45 | -6.7778 | -47.8763 | 2026-09-17 15:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6890bc8b-75de-303b-b153-f47b4de75bfd | -8.4983 | -57.6271 | 2026-09-17 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 2c77f55c-439e-34b1-94f6-04b219b277a9 | -8.58 | -44.5552 | 2026-09-17 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| cca98be3-f6df-3778-8038-550d0d9c0cae | -9.0868 | -61.0095 | 2026-09-17 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ee0665b9-1188-3024-b7a7-921dad024056 | -7.1384 | -42.1529 | 2026-09-17 15:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 7c180181-2a6a-3995-ab5c-72ced8ba7526 | -12.7515 | -51.2639 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 191540c4-5886-3ec9-a743-4e6790b9d893 | -15.5393 | -53.8292 | 2026-09-17 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fb6a91d6-e72b-36ed-ab16-c803afcd8105 | -8.5239 | -44.5153 | 2026-09-17 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 6ee4a43b-a4cb-3f05-b687-c890f564f2a1 | -10.3769 | -49.9723 | 2026-09-17 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1f42ea38-fb29-33ad-8056-dc174abfff37 | -14.8183 | -59.5532 | 2026-09-17 15:10:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3117b6cd-76fd-38d2-b73a-fb666d79435a | -6.6703 | -43.6337 | 2026-09-17 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| bd21206c-ac98-365e-8952-e825559aa65a | -13.166 | -51.6602 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ad4bf6a6-48ca-3224-96e1-7da2549081e2 | -6.7648 | -59.4408 | 2026-09-17 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1c0316f5-7787-378f-bb12-2ecdcc7d631b | -6.5837 | -58.8498 | 2026-09-17 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4ef8e9bd-d271-3d46-9a86-21ebd4687ed0 | -8.6188 | -44.4819 | 2026-09-17 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| a06f101c-71ab-3780-9842-45b2511ea639 | -15.5397 | -53.8081 | 2026-09-17 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7d9c462d-841c-312b-980c-2456e7ed21fa | -9.7794 | -60.4551 | 2026-09-17 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3730cc92-b57a-33ee-89f9-d1b6382fe1fe | -12.7243 | -48.2734 | 2026-09-17 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 26eeac85-e47c-39a6-8bab-14791171031f | -7.8033 | -44.8651 | 2026-09-17 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| fbc39dcd-016a-38d5-85ba-6f8a181756df | -11.3161 | -46.7699 | 2026-09-17 15:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 3256e666-f349-3372-9615-7f6a2f4b0b6c | -8.8644 | -45.8919 | 2026-09-17 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| ee74996e-5cc7-3b65-b9cb-10e490fe7dc5 | -14.1932 | -45.1606 | 2026-09-17 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 909c95a9-4d3d-36fc-aca4-fbd0970a5c52 | -9.852 | -46.9046 | 2026-09-17 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| a43c2922-8ffd-3d4d-be25-2df20aa2722c | -5.7419 | -51.7422 | 2026-09-17 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| 24347fc6-0534-3ae5-8afe-32d68aac3c80 | -11.8941 | -47.5876 | 2026-09-17 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 767e4622-b37b-32d0-a377-4e51918c51af | -9.4325 | -50.1299 | 2026-09-17 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4779bad1-61e4-39bd-99a1-dcb3dc22fa94 | -14.1547 | -45.1442 | 2026-09-17 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 2d9d63c5-793a-37a5-99ca-4f5b2a96b0ae | -13.3754 | -51.7406 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2e5c939c-5b0b-3cfd-8148-9e47d546bf03 | 1.2609 | -50.8928 | 2026-09-17 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ace1cde1-f486-3ab1-bec2-8208c5a9e44d | -11.2302 | -54.119 | 2026-09-17 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 96c1df2e-6977-3dc1-aac5-f2089b79e3c3 | -7.8221 | -44.8632 | 2026-09-17 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 1e4f61c3-40f1-3822-9fe5-4307240f936b | -18.8906 | -46.8284 | 2026-09-17 15:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2cf2155c-c6df-3db3-9f93-d26fef8b7ac2 | -14.1937 | -45.1372 | 2026-09-17 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 47efff1d-00a9-35e7-9e31-ae18d294f8d5 | -14.1742 | -45.1407 | 2026-09-17 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| c8d682d2-b0f5-37a4-b12c-ab4cb52e2317 | -14.8376 | -59.5515 | 2026-09-17 15:10:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b1120ae4-a080-393c-a865-95ca86075d0f | -15.539 | -53.8502 | 2026-09-17 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ac851ecf-1ab3-3e9a-907e-39511d06b194 | -11.2693 | -54.0129 | 2026-09-17 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 82c9c40f-70df-3fda-b150-79b454a86d6c | -13.6526 | -45.993 | 2026-09-17 15:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3f1e2999-c1ba-36b9-9fa7-386e98d69945 | -8.8647 | -45.8693 | 2026-09-17 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.4 |
| c297f65b-8b70-3b0f-98fd-45a0ac2828c0 | -4.5229 | -54.9639 | 2026-09-17 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| b3b84bae-a339-3f2c-b752-8d5be4aa49d8 | -13.2239 | -51.6318 | 2026-09-17 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 94fe0289-831e-3eb8-ae6e-0b138673f5cb | -11.8924 | -50.0823 | 2026-09-17 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |


[Clique aqui para ver as próximas entradas](README97.md)
