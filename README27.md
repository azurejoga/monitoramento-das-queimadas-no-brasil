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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c94583a6-8f49-3383-991f-b8569284506d | -10.96507 | -49.57481 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| deea449e-ebb4-3de2-b145-2d134b6a0186 | -11.74119 | -50.11081 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 413a31db-5e1c-331f-ae9c-a8f75cfc3773 | -12.53432 | -46.98633 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd166f15-4ebe-3e26-a542-22f28432f513 | -12.58375 | -46.9806 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b5e88c1-3a90-398d-a84f-9beba65f885f | -12.52911 | -46.9818 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b7ce5e3-145b-3095-802d-302528020cd7 | -9.46942 | -57.84036 | 2025-08-13 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 857b00d7-71f9-300a-9802-26395b53a128 | -16.5091 | -47.85374 | 2025-08-13 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69065494-5be7-3cf8-94db-4b3f22bf597e | -18.53183 | -46.05429 | 2025-08-13 05:08:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1ae90530-9da4-3da0-b246-9d4a74aa6da6 | -9.92158 | -65.23672 | 2025-08-13 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21730b12-38c9-3855-9f37-8c5a4e885d92 | -12.31773 | -46.0492 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be42e9c6-b4f7-3d45-aad8-b11f6826f620 | -11.76241 | -48.19104 | 2025-08-13 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03b7193d-5b3b-30ff-80ee-658a4a7eba8b | -12.52958 | -46.97794 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dfa26f3-2dd6-306c-9f21-c13eaf8c6980 | -16.29494 | -52.91513 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11bd5159-e0e6-3c58-a0fc-8af250c53d64 | -16.31655 | -52.91516 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 876d9b08-caa7-39c3-a921-6db52bf741e5 | -11.73202 | -62.33084 | 2025-08-13 05:08:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8dd08bd-8654-3c73-b839-31bd289d7f40 | -9.47326 | -63.52019 | 2025-08-13 05:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc379062-dc65-3c76-8e18-b38ea3457889 | -12.49701 | -46.9615 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61dc1786-986f-38f0-a167-721ebf74eb73 | -12.30525 | -46.05183 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08287d6f-293f-37c6-a4d4-7a065da84f01 | -16.91165 | -48.1496 | 2025-08-13 05:08:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13856f9d-1216-3e66-b141-4cf4e95e9a7c | -10.29871 | -57.12326 | 2025-08-13 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0404821-f67f-326e-85f2-209845df4ab6 | -11.68498 | -50.14323 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22969d4c-76db-35df-abae-a13cdbb4b5a6 | -12.32372 | -46.05005 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a305f2af-c49f-3da1-bf39-3852bc7fc0be | -17.05157 | -51.79484 | 2025-08-13 05:08:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb369185-fec1-3525-9706-3f15991af28b | -12.47741 | -46.96448 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0743279f-b303-3662-9496-b7a5b23cd015 | -9.18721 | -59.67017 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42266c1d-6cd1-3ffe-8e0f-3c4d36b5617c | -12.57894 | -46.97249 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b14900d1-cb7a-38ce-8c14-5df9f0b9df56 | -12.51873 | -46.97242 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c142249-058a-365d-a9c1-f9b826401edd | -12.30361 | -50.01006 | 2025-08-13 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b014a233-d07c-3825-9ff0-794ef51ba777 | -10.97165 | -49.57399 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c57e09e1-3f0b-3b4c-a302-14a75cdb4c00 | -16.31253 | -52.91452 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d1e9cc3-803e-339d-ba20-d677fa265d28 | -10.4156 | -54.40614 | 2025-08-13 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9452d31-1acd-3c7c-ba1f-864c13246351 | -10.00635 | -59.21472 | 2025-08-13 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c03cf7f6-2296-30c8-a408-eb47a9931e06 | -11.90518 | -52.53411 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d446f69-691e-37ce-a59e-53481cb87e84 | -10.47634 | -61.32177 | 2025-08-13 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cf9810c-5ad7-32ef-8216-d0c022a5a7c5 | -12.48002 | -46.95911 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 314f0141-e4fe-38e0-937a-209c7d6ed626 | -12.49655 | -46.96536 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90203309-49f2-3fc4-8182-b2dce1d01eaf | -11.64309 | -50.14669 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaaab7b3-0497-3771-bd5d-5b4a8a992daa | -12.58072 | -47.05518 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfebf86-87dc-3339-ade1-08cb120904b7 | -11.90061 | -52.53845 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a667ec15-adeb-3fc8-9e06-396dbeb2029c | -9.38091 | -61.53646 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4dc5058-d6e7-3838-804c-f91c8b61210c | -12.30964 | -46.0662 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86f01135-10f2-3efa-a815-704b284c6305 | -13.06925 | -56.84603 | 2025-08-13 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 744d4bbc-9a26-368e-8253-31c29eb2004d | -16.29896 | -52.91566 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d733b1b-d884-31fb-bab3-280823fd002e | -9.18864 | -59.66154 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 472f578d-f09a-30bf-a853-0ec50550d864 | -12.52392 | -46.97715 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd8e37ae-d585-3696-bdee-aaf951df4d0f | -11.91294 | -52.53522 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6427ce6-06fd-30ae-b8d7-87fcc9e198d7 | -9.06248 | -60.66076 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f2e5320-961c-3e76-9b10-2d85e579bca2 | -10.34344 | -64.47076 | 2025-08-13 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c14e68-c842-39c6-b50c-313ed3ed276f | -16.29426 | -52.92014 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1340fc4e-d32a-3ee8-aa98-c54b50e523ec | -16.29092 | -52.91456 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 696f9f52-3538-360d-aa27-9f2671dbcf19 | -8.93433 | -60.72721 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb2be9c6-fc1c-3eec-9229-293e1ccbd230 | -9.3781 | -61.52851 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d82cc7d-9d67-3e93-a5e0-d64e76894f6d | -10.96235 | -49.57273 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 39f7d3f2-0529-3965-aa9c-ebe8579a38b7 | -16.30385 | -52.91832 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 685aa736-383f-3e1e-aaf4-52acb75f5ea7 | -12.50787 | -46.967 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7112ebda-2197-3c14-813b-459ccdc069e8 | -8.93822 | -60.72791 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8793fc6b-c185-33a5-bda5-8a06fa5db82b | -12.52345 | -46.98105 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb228cc4-75a0-3ae3-a147-f012128d1336 | -12.32757 | -46.06886 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97041d57-9461-3977-a7d0-9d2980d98b80 | -15.09477 | -51.34961 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f98026d-a078-3c95-8d1f-57430ecc786c | -12.57852 | -46.97606 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87638786-8efa-3f55-b808-96459430b3c8 | -9.38154 | -61.53284 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b8c5d66-46ce-30f3-adac-3ecaeb6cef82 | -9.19888 | -59.66782 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa8e999-add7-31d5-bea4-2282b85c04c1 | -18.05323 | -47.94104 | 2025-08-13 05:08:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f538fee6-3258-33f3-b504-695c0da229b7 | -9.3828 | -61.5256 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 039d15e7-f8be-3357-abac-45ddb094d095 | -9.51044 | -62.37325 | 2025-08-13 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68d788c4-be78-329c-9ffe-21bde3b9b8ed | -9.38968 | -61.53426 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032612b9-3d6d-3a9d-8964-2fc57a5eaf4b | -12.51307 | -46.97162 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b112af12-ce90-3161-a10d-6c30c9163e02 | -9.27675 | -60.76719 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aec66132-5b81-31f8-8c39-2f4e4a42bc76 | -10.967 | -49.57336 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 71f40fc6-8b54-3893-8543-0c719763a822 | -12.31175 | -46.04833 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b2dce8-a5ce-3cfa-a0a0-2a561303c4f7 | -16.31187 | -52.91962 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 112451ee-ec5b-3c4e-bc42-ad01d5952a78 | -16.311 | -52.91749 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 603f15d7-6010-33bc-9876-7f66ffa018f9 | -12.57809 | -46.97978 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11f9a506-99f8-3cc0-811b-73e73b257682 | -12.30576 | -46.04744 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2914bac-c4a1-3fc2-acfe-effa502277c5 | -16.31587 | -52.92028 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 82a21d80-51ef-3062-9fa7-e81ad82816c0 | -12.30296 | -50.01484 | 2025-08-13 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb688b9-fa58-3a22-ab0a-d58cc9e3c6d4 | -16.29165 | -52.90924 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8a47105-cac4-388f-bad1-f92c3e58ec89 | -10.34708 | -57.60118 | 2025-08-13 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8575b8e7-81fd-3e68-87c3-2a58be019f36 | -11.74059 | -50.11544 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8225c07-d4e5-3b8e-a1af-0f7902024394 | -15.08983 | -51.35332 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1c63fd3-9b3f-3bdb-b608-bbfd9bc023dd | -12.30214 | -50.01167 | 2025-08-13 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c1db614-ef45-325b-b649-a45588570490 | -9.1682 | -59.67144 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9c09e14-4705-3466-b960-4527321a2f8a | -15.09858 | -51.35452 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b083f15-633e-331c-ac9c-28019c6f764f | -16.29581 | -52.91717 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28d491bb-e6d8-3c53-b40c-b03c59433349 | -11.71664 | -51.60979 | 2025-08-13 05:08:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e58615b-2120-3ee3-8f45-357198327a77 | -16.38792 | -50.9012 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 291206e2-6012-315b-8a05-afa17b544919 | -12.58236 | -46.99249 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c79e878b-9ea1-3a7d-a0bf-b74c08dffaf9 | -9.05963 | -60.64812 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d0003b63-499a-3cc1-af51-77f5fd041272 | -10.58013 | -55.41371 | 2025-08-13 05:08:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59eef98a-8246-3bfb-a56c-3a75d49cec6c | -12.58222 | -46.97129 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cabf82f-9557-3cbc-a256-12c602f4cbe2 | -11.90906 | -52.53467 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55d2bf9e-e337-3aeb-b676-f2d380bc4e24 | -16.29967 | -52.91047 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ca30c4e-e033-37a9-9cdd-efe35bc2d8e3 | -16.31431 | -52.92319 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a6ab2978-4c2d-3ba6-9990-5a5ef0ab7a74 | -11.63406 | -50.14542 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5bec7853-5c09-3965-82ee-70eac04d8f7f | -10.96042 | -49.57416 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daa666d7-5322-3991-ac08-2aae257ffa87 | -11.64193 | -50.14936 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a29e442-9bc2-3088-855c-ace2fe361297 | -10.97036 | -49.57062 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f245f37-7789-3fe8-a9ab-6a6a7a5b0263 | -9.82638 | -60.76457 | 2025-08-13 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47358e85-0185-37af-8b36-e58a1eaaa372 | -9.51472 | -62.37402 | 2025-08-13 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975af441-ccbc-338b-85d6-929223148977 | -9.38217 | -61.52922 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
