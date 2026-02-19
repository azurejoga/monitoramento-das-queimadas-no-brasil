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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1edf751-44a4-34a4-8143-4fd4a6c75253 | 0.9207 | -60.2579 | 2026-02-19 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c8686647-741a-3b59-9e8e-f6251df642f1 | 0.9389 | -60.2578 | 2026-02-19 00:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 6a7f14b7-343f-310a-a8a0-bc9c2b9b38eb | -14.51783 | -43.62664 | 2026-02-19 00:05:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11a46c83-c801-3824-aaa9-62c731c0a216 | -13.49202 | -41.132 | 2026-02-19 00:05:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b5d56636-92ef-3690-9459-d8a283953d5d | -15.6765 | -39.80423 | 2026-02-19 00:05:00 | TERRA_M-M | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| aaebee39-8fba-32c2-876c-a4424e806163 | -12.98951 | -41.19569 | 2026-02-19 00:05:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d894b7da-6151-3dd9-a235-2e84b816f5e7 | -12.98774 | -41.18408 | 2026-02-19 00:05:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 81b36a17-9fc8-336e-91ba-a46441103a2a | -15.91188 | -41.7355 | 2026-02-19 00:05:00 | TERRA_M-M | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| da912057-b510-3493-8bfb-6fd0f9c2feee | -14.51911 | -43.63575 | 2026-02-19 00:05:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e7baec5-a6f5-3c13-a4e8-3cd508448a98 | -13.40998 | -43.75214 | 2026-02-19 00:05:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 586311b1-ddf1-3f5e-b94e-45b7ddb01081 | -13.50601 | -46.70953 | 2026-02-19 00:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c00bf25b-2d38-329a-919d-8ec36ab5da8d | -15.85395 | -43.50559 | 2026-02-19 00:05:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e1565dc-db90-3a16-b91f-3d40837e4fe7 | -18.35497 | -40.01967 | 2026-02-19 00:05:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| bad160b3-a60c-370c-bf7a-c6537483ee28 | -14.53431 | -44.40923 | 2026-02-19 00:05:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44a78262-fd7e-3d2d-9b30-b7685ff91bea | -20.75662 | -41.68999 | 2026-02-19 00:05:00 | TERRA_M-M | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d4ea2a1e-86ec-3a2f-8d7e-ce7d630a0d61 | -13.3032 | -40.90218 | 2026-02-19 00:05:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 53559fa5-dee3-3b67-bb6f-1cf3a59963c8 | -9.56679 | -44.60135 | 2026-02-19 00:07:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97bc8330-d396-333c-81b4-5b4a8eee9c37 | -11.88152 | -45.28931 | 2026-02-19 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 066f217b-2c82-34ce-b45e-85fbbe50c2d0 | -7.24395 | -43.08793 | 2026-02-19 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1c522fb4-7129-315e-ab28-2ef0ad4d345d | -12.49419 | -43.65473 | 2026-02-19 00:07:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0887917d-4bcf-33f8-88f0-89d9185cfa69 | -12.0796 | -43.53071 | 2026-02-19 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 482ea6a8-aee6-3812-abd8-65849420b220 | -12.48246 | -43.64398 | 2026-02-19 00:07:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66a740d2-1855-3b7d-b367-b60ec5a1d102 | -12.39312 | -43.66341 | 2026-02-19 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c64e5e2c-b97a-3c84-b241-9cd653437cf0 | -7.24704 | -43.08126 | 2026-02-19 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| bc8ef22e-2f25-3d47-8925-dbd6c7f2d572 | -12.24394 | -44.23698 | 2026-02-19 00:07:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be12d19b-8e31-3206-8f79-ad8dd618078d | -11.89123 | -45.28199 | 2026-02-19 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acfd6dfb-aae0-3232-a352-dea9cfd759de | -11.89245 | -45.29103 | 2026-02-19 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb9e472d-6fee-3f47-9dde-63e89d7c42ee | -12.48375 | -43.65319 | 2026-02-19 00:07:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3350e789-5471-37e1-821c-5092f571b9e2 | 0.9389 | -60.2578 | 2026-02-19 00:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| acba68cd-2796-3a61-b3f6-c10ee5d30931 | 0.9571 | -60.2577 | 2026-02-19 00:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f8d00e7c-6778-3aa8-99cf-708f5a5edeb1 | 2.5252 | -60.717 | 2026-02-19 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c92a0b81-265b-3f14-9cdf-5079c996f330 | 2.5252 | -60.717 | 2026-02-19 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8f36b516-47eb-317f-a5e7-fc56c3c49b4d | 0.9389 | -60.2578 | 2026-02-19 00:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e0c09590-6b8d-3114-8de5-9ec41843b3b7 | 0.9389 | -60.2578 | 2026-02-19 00:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cfbabf49-b75e-3907-bfb7-1403ecb38b39 | 0.9389 | -60.2768 | 2026-02-19 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 20157e25-d1c4-35fb-adef-7dd58b5dea4a | 2.5252 | -60.717 | 2026-02-19 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3e5e94fa-31ed-31b6-917f-289843ba7e0e | 2.5252 | -60.717 | 2026-02-19 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d58697b4-1a23-30fb-82df-7eaba303064f | 2.7088 | -60.2398 | 2026-02-19 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7f460b8c-f0c4-3f6d-ac11-cf7ef56ec90e | 2.6905 | -60.2401 | 2026-02-19 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9ebf8e71-8c8e-30e0-829d-415a2eca081e | 0.9389 | -60.2578 | 2026-02-19 00:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 24124486-e618-3fa3-9e3c-527b8145cc81 | 2.5252 | -60.717 | 2026-02-19 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3baee223-0ab3-390a-bf6d-3d44cf05ff98 | 2.5435 | -60.7167 | 2026-02-19 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c3abf34b-408f-3ed7-9b35-2df10e1792c2 | 0.9389 | -60.2578 | 2026-02-19 00:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1a07f351-acf7-30d8-9882-fdca3e084abb | 2.6905 | -60.2401 | 2026-02-19 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 07114fdd-91db-3334-9543-80b1cfb15c20 | 2.6905 | -60.2211 | 2026-02-19 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a60bd39a-44bb-3178-8887-d54a24eb08d5 | 2.5435 | -60.7167 | 2026-02-19 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b61ff79a-ef69-3872-8160-6c68fb0ee0fb | 2.5252 | -60.717 | 2026-02-19 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 271dd39a-d626-36de-9d40-91e4a995c022 | 2.6905 | -60.2211 | 2026-02-19 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 5f6ceb38-80d1-346e-8a03-02c1d96e660d | 2.7088 | -60.2208 | 2026-02-19 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 963a2e0d-13cc-3c5d-8925-9bfed57b39b2 | 2.6905 | -60.2401 | 2026-02-19 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 144.0 |
| a8e3c3c7-96fd-3be7-98fe-8f6d7fa9d54f | 2.7088 | -60.2398 | 2026-02-19 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| dad4418f-07ec-3cb2-a168-f084e2ff859e | 2.5434 | -60.7357 | 2026-02-19 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b9998795-aed1-3234-a7d5-b1f01324bdc1 | 2.6905 | -60.2401 | 2026-02-19 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 19a7903c-783f-3fc9-bc68-270cb69347ff | 2.6905 | -60.2211 | 2026-02-19 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a8206f58-d0a6-370e-9c13-4112ca98e121 | 2.7088 | -60.2398 | 2026-02-19 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1238e7f8-bd26-3f6b-9e53-c6b2eacfb241 | 2.5252 | -60.717 | 2026-02-19 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a1fcaa34-616a-3551-b82c-322afe1a00d0 | 2.5435 | -60.7167 | 2026-02-19 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 8bd34bd2-fdd9-3753-9e51-7c9880e0379d | 2.5435 | -60.7167 | 2026-02-19 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| c68da61b-c75a-3c6b-9da8-c5ba59f939f7 | 2.6905 | -60.2401 | 2026-02-19 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 92c4eb83-a126-3acb-a66a-9c9376efcac9 | 2.5252 | -60.7359 | 2026-02-19 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| be2b2aaa-78cf-3bcd-bdd3-df5f18343eef | 2.7088 | -60.2398 | 2026-02-19 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6240ec9e-3fea-310a-9a74-0e0f056ec443 | 2.6905 | -60.2211 | 2026-02-19 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 327e8483-8fba-3cd6-9ec1-6ea0ed2ea312 | 2.5252 | -60.717 | 2026-02-19 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 117.5 |
| c7d1e324-63c6-3655-b495-d6cb194844a1 | 2.6905 | -60.2401 | 2026-02-19 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 6cc6f39b-09eb-39b2-8639-b72c75638a93 | 2.5435 | -60.7167 | 2026-02-19 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d711e036-a3cd-37d8-ad97-ebf7cf868536 | 2.5252 | -60.717 | 2026-02-19 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 57d23b30-9f65-36d0-97ab-91e7f89fc626 | 2.5252 | -60.7359 | 2026-02-19 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 21e4dbcc-1060-3eaf-b102-e68c48209f6e | 2.7088 | -60.2398 | 2026-02-19 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 24a8d3dd-1e97-3786-8ac9-d9adeaa04519 | 2.6905 | -60.2211 | 2026-02-19 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b03d6595-f971-3ec2-a3df-f81507251462 | 2.6905 | -60.2211 | 2026-02-19 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 74d53b2a-2a4a-35c6-8e44-327017bdd3fc | 2.7088 | -60.2398 | 2026-02-19 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2e743994-e144-315a-8cf9-8f12c064a505 | 2.6905 | -60.2401 | 2026-02-19 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 7ce70237-3df5-3cdd-a67e-6370db99681b | 2.5252 | -60.7359 | 2026-02-19 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d7b78bdf-1ab2-3806-83d9-cbd28752ee68 | 2.5252 | -60.717 | 2026-02-19 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 115.0 |
| bf5cf3eb-be84-3197-bd8d-ed243c2f308a | 2.5435 | -60.7167 | 2026-02-19 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 20f09069-fcb3-3f83-8e04-5605691a1694 | 2.5252 | -60.717 | 2026-02-19 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 2391cfea-7df8-3de9-9365-3960f6e6daf4 | 2.7088 | -60.2398 | 2026-02-19 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 45d4936b-156f-3117-a4a6-5ff24256cdd8 | 2.6905 | -60.2401 | 2026-02-19 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 879527a1-d3d5-3291-b286-bb9d19e8caf3 | 2.5435 | -60.7167 | 2026-02-19 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 89dfba96-0213-3d48-9a61-ba0bb62c4298 | 2.6907 | -60.164 | 2026-02-19 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c6a751da-9d37-3399-bd55-62cd3a48fa48 | 2.5252 | -60.7359 | 2026-02-19 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f48969c3-1391-3869-8319-4ac6b595f88e | 2.6907 | -60.164 | 2026-02-19 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c631dd0d-5ee6-3bd7-986e-9d794b047e95 | 2.5252 | -60.717 | 2026-02-19 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 0b9beba0-18fd-3d85-9d9b-312ca95c20f1 | 2.6905 | -60.2401 | 2026-02-19 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| da8fa900-5b1a-3460-9e05-9b11fac16334 | 2.7088 | -60.2398 | 2026-02-19 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 75087320-ddb1-34a3-9d8f-620f8d10e0af | 2.5435 | -60.7167 | 2026-02-19 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 895da75f-e997-3a71-ac5a-c4aa5d860180 | 2.5435 | -60.7167 | 2026-02-19 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e4483541-13b6-3136-92bb-7492c90b0b47 | 2.6907 | -60.164 | 2026-02-19 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 421110fb-b6ba-371e-b460-e25a6e1143ca | 2.6905 | -60.2211 | 2026-02-19 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 50e6ba7e-c910-3d5a-977c-bc6befb56248 | 2.6905 | -60.2401 | 2026-02-19 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9eb493bc-b5de-31bd-ae0b-bd7b330c86a6 | 2.5252 | -60.717 | 2026-02-19 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cdabb3a7-c3ee-3242-96dd-c00a1707fe08 | 2.5252 | -60.717 | 2026-02-19 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 471ff8c8-c193-347b-967f-b0798cd8c441 | 2.7088 | -60.2398 | 2026-02-19 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ca98d598-6bfe-3f51-a0f8-9728e493a0e2 | 2.6907 | -60.164 | 2026-02-19 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 6f2ce609-8040-3371-8d40-0eef7816a92c | 2.6905 | -60.2401 | 2026-02-19 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 8f094853-2f8c-339d-a305-ba11b302b3ac | 0.9389 | -60.2578 | 2026-02-19 02:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e8281531-3bbf-3ab0-b439-910cd8cace6d | 2.6907 | -60.164 | 2026-02-19 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ae5f3996-ae28-3b45-8c46-8d531dd34dad | 2.6905 | -60.2401 | 2026-02-19 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8883ca74-6f3c-3d80-828e-2db49fae1cc7 | 2.7088 | -60.2398 | 2026-02-19 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 3f8fcaa1-2c04-3fb7-a917-1d7dbe9a773d | 2.6907 | -60.164 | 2026-02-19 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |


[Clique aqui para ver as próximas entradas](README2.md)
