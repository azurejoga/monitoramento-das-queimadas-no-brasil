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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a92d31e2-f2c6-3cdc-9b03-ccbbb306f35b | -9.9266 | -60.7171 | 2026-09-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 218.5 |
| e13aa5ab-a5c3-384e-8c88-c6254610c09e | -5.7388 | -45.0172 | 2026-09-28 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| b88967b0-e925-3687-a46a-e57e211104f6 | -12.1202 | -57.1767 | 2026-09-28 18:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 476ec593-b4ca-32c3-8489-ae4e4e1c51e5 | -7.3175 | -44.591 | 2026-09-28 18:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c72c1abe-ddef-385d-8bd9-16e0578ecf44 | -10.2067 | -49.9898 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.9 |
| e23b5375-10f2-33af-8c76-d01d521ab20c | -10.9445 | -43.8849 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 231e700a-e9f9-3342-912d-4a20d6a3c8be | -11.6096 | -44.1382 | 2026-09-28 18:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| c1202c93-6de3-3c57-9f50-916f5f8825e2 | -6.314 | -43.5946 | 2026-09-28 18:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9007dca1-beb8-3887-a2a4-ccbc6668419c | -10.2065 | -50.0113 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 5288cf59-0b94-3ee1-8925-9d044fb3961c | -5.4762 | -45.1262 | 2026-09-28 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 196.1 |
| f800050b-b9c1-3fff-9f55-703a5fbfd3b6 | -11.1331 | -50.0409 | 2026-09-28 18:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| bdeb049a-f547-3fd1-a7af-ad4a3b2683e7 | -12.6267 | -47.2851 | 2026-09-28 18:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| a265d9be-11ee-31da-9529-695fd18dd3f4 | -9.0437 | -49.6317 | 2026-09-28 18:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| db8d2dde-2260-304e-aa4f-2c7dbf769905 | -9.1682 | -45.7684 | 2026-09-28 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ddad8ffe-a5d6-3131-a1c3-cda1518aa3bc | -11.1775 | -44.7832 | 2026-09-28 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 1fd45535-5866-3b21-916b-789bb28c0642 | -12.9649 | -51.0671 | 2026-09-28 18:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 902.6 |
| 31f40700-4743-301a-9234-c9fc7f800030 | -11.3739 | -43.3972 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2662ece2-a491-36e8-868a-3d22448be338 | -12.0019 | -57.6051 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| d603a380-e7ec-3060-bef8-a7258e4c768b | -8.2807 | -54.7158 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 222.0 |
| 11f39b3a-9491-33d1-874c-499a651a964f | -11.1327 | -50.0624 | 2026-09-28 18:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b8d7cdac-a035-3cff-9755-e6a4198b34d6 | -10.2254 | -50.0093 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 208.4 |
| ac1fa90e-a56b-3278-b1dc-ba7e437d275a | -8.2804 | -54.7562 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 68cac730-24f3-35e6-963a-1b5ab5aa2412 | -11.6994 | -43.4178 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 7590a00d-3168-3b68-a39c-aa5ba6974f68 | -7.6852 | -54.7532 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 399f37ae-9afd-320b-a9fd-d8f7cdd0434c | -10.8001 | -57.2007 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 0e9fbc9a-3b18-34e8-a857-f90d2e7bb405 | -10.6869 | -44.4576 | 2026-09-28 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7be84b90-27a9-3091-97a1-bf76e917a427 | -12.6262 | -51.9573 | 2026-09-28 18:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 367b6b40-a904-396c-88e6-41355fd2d779 | -10.9637 | -43.8821 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| f533f9ed-94b5-3edd-a2f3-9991455445c7 | -11.3817 | -47.4322 | 2026-09-28 18:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 11319b7b-77b6-3310-9cf1-48d814c36256 | -13.6866 | -56.6131 | 2026-09-28 18:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a0e55b78-8e38-3318-8f55-a8f96dde1be0 | -8.9428 | -63.2797 | 2026-09-28 18:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 104.2 |
| c6c5c479-bd5d-381a-b4f0-088327247c45 | -10.1098 | -50.1921 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 842ecc09-35b5-3ff4-a566-3766d5e82daa | -9.1525 | -49.9639 | 2026-09-28 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 97200dbe-c10c-3f12-89be-ddd6a6ad897c | -12.9109 | -52.0719 | 2026-09-28 18:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 98c3aa27-7314-312a-a656-81e2205178dd | -11.3922 | -43.4417 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 521.6 |
| 704ad515-6037-3a28-8fb7-ba04268a34b2 | -11.8641 | -47.1004 | 2026-09-28 18:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3cc2527f-8867-36d5-bcff-88333ed90936 | -6.3137 | -43.6178 | 2026-09-28 18:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7562547c-e4ea-38e9-9a6c-1ae27327907e | -9.0969 | -49.9049 | 2026-09-28 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| d9a41b6f-529e-3ba4-8c5c-6b63c2a2d933 | -13.3262 | -43.976 | 2026-09-28 18:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| eff6002b-05aa-3b41-8a0b-b469cceb636b | -11.6209 | -46.7967 | 2026-09-28 18:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 242.0 |
| f324a0d9-ecb1-3561-9f24-a4138619a98f | -13.3272 | -43.9285 | 2026-09-28 18:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 96c56a6e-f288-399c-a0a6-5ebeda15c05e | -11.3927 | -43.418 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.7 |
| fe51f0aa-c119-33f5-8965-35055d83668b | -10.8191 | -57.1795 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 218.8 |
| a76c2b25-4298-34b8-bc63-61a83a4ea49f | -11.373 | -43.4446 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 7b3b8703-ba00-308d-9b13-ff105ba44133 | -15.3998 | -47.9261 | 2026-09-28 18:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4316acfd-fe66-30c5-b174-81cf22aa5183 | -9.9453 | -60.7161 | 2026-09-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 70bbb3b1-1ca7-30fd-ac47-78a22e49f853 | -11.7178 | -43.4623 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 49c25406-c8e9-3bad-a934-043db7898c65 | -10.8379 | -57.1781 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 346f1a3c-407e-349d-a25f-7b27687a4992 | -5.4764 | -45.1035 | 2026-09-28 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 140cdaca-0546-38f7-a5f6-f52483c2f250 | -5.4949 | -45.1249 | 2026-09-28 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| aa370ace-67ad-30d4-bd75-242aaa56267e | -7.9082 | -54.7597 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 1596539e-34f7-3998-a06c-efa60710c625 | -11.6213 | -46.7742 | 2026-09-28 18:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 213.6 |
| a1a5685f-25eb-3abd-9cfa-7747262fa55e | -12.702 | -47.3638 | 2026-09-28 18:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| f64baa31-194d-3146-9999-d23726d51898 | -7.3306 | -54.995 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| fabbdf1f-8b72-30c3-af2e-e11364bfd3dd | -11.699 | -43.4416 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 1ad333ed-cb51-336c-89af-b41920b6292f | -7.7038 | -54.7521 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| dceb5b67-1536-3ba6-b673-298f4a2b0156 | -12.588 | -51.9617 | 2026-09-28 18:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c5d336fb-c64b-3177-b63b-4790dd66dae4 | -12.6832 | -47.3442 | 2026-09-28 18:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8f006dd1-5a9b-36fc-9c23-e3f4ea01e802 | -14.0915 | -46.3096 | 2026-09-28 18:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4ee1f699-9c20-38f2-bee8-383df7dff902 | -14.1304 | -46.3031 | 2026-09-28 18:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3377751f-43d8-35b5-9cf5-6ed23e79253f | -11.5904 | -44.1411 | 2026-09-28 18:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d5003398-8ab1-3948-b716-91c2202c5c01 | -11.1966 | -44.7805 | 2026-09-28 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 36dc5f04-680b-32bb-8875-c65f630d0750 | -10.8052 | -60.7257 | 2026-09-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 342d73a5-171d-3662-8a07-a803e6d80ffe | -15.0199 | -51.3939 | 2026-09-28 18:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| cd730420-a0b8-346b-bd1f-ac887daad2f9 | -10.8187 | -57.2192 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 195.1 |
| fa10b7c3-2210-3ba3-9141-2eca4fc262dc | -12.9461 | -51.0481 | 2026-09-28 18:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| db603cd4-95ed-320f-b9fe-703ac384dc27 | -10.8373 | -61.3988 | 2026-09-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| feb381b0-6dee-3246-9d05-c142c290714f | -7.0674 | -55.4896 | 2026-09-28 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 5cc6172e-8214-3cfb-9f47-6246a83398e6 | -10.8184 | -61.4191 | 2026-09-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| a04d865b-565b-37a0-b009-8fa638c7f6f6 | -11.6986 | -43.4654 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| fec6a04d-ece5-35a7-ba2a-67ef941ac0a5 | -12.9457 | -51.0695 | 2026-09-28 18:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| d01c1ac4-f58b-38c5-963d-7e995c56bb48 | -12.6071 | -51.9595 | 2026-09-28 18:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 4b0a5da7-2f0e-3533-b472-336d1ad34706 | -12.8061 | -54.0048 | 2026-09-28 18:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| d214fef4-df73-36b3-80c3-ae313f1d6ec3 | -5.7384 | -45.0626 | 2026-09-28 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| cb70c7e7-76f2-34f9-92ff-16648b560db1 | -8.2992 | -54.7348 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 306297a3-e217-37b3-b928-db6e23332187 | -9.0783 | -49.8853 | 2026-09-28 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 59b2cc34-81ec-341a-8c93-d5272a7869cf | -15.4003 | -47.9035 | 2026-09-28 18:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b39ebdc3-745f-33a2-a8c5-5457e969c628 | -10.207 | -49.9684 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fc7c09f4-d6fa-3866-96cb-06f57e74fae5 | -9.9784 | -50.1412 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 5edc0487-0e4d-350e-bc8f-5023deb7fe5a | -11.3735 | -43.4209 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 7c711eb1-30fc-3286-89fa-cef4bc5ddc15 | -11.983 | -57.6066 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 6a374eee-4c29-3430-8be5-4d899d9418ec | -8.1871 | -54.7824 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 737394e9-7522-3a28-a48a-2b6fb5f12aff | -10.8106 | -48.7355 | 2026-09-28 18:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| df967c93-42d2-378f-8a5b-f5a78cf6a71a | -9.6864 | -58.1258 | 2026-09-28 18:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 3cf0128b-beb7-3905-86a3-4e8be31c59c4 | -8.1869 | -54.8025 | 2026-09-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 22f6398b-4438-352b-8b98-38bacbb03b05 | -9.9396 | -50.2304 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f9a21fd0-69ed-33c3-9016-02f48a843eb9 | -11.9039 | -47.0053 | 2026-09-28 18:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 108bb9a2-8635-30dd-aa14-ef432fc72a8e | -11.0991 | -51.1111 | 2026-09-28 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7ed7b1b5-2bdc-3a47-bc89-b583b1096893 | -10.6505 | -50.7123 | 2026-09-28 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 3e31b5f1-ffc9-3351-a7fc-95a95f15c617 | -9.9781 | -50.1626 | 2026-09-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 436dd54e-aac8-355a-8006-040a20a894a9 | -10.8189 | -57.1993 | 2026-09-28 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 416.1 |
| 207687d1-c8f0-3f0a-993a-7cb453d91b82 | -10.9441 | -43.9084 | 2026-09-28 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 01c5e04a-85a2-3c9c-ad68-bff513522c17 | -11.1962 | -44.8037 | 2026-09-28 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| a391c1a0-c12e-3e83-9b50-a03affd2b9da | -9.7684 | -44.8312 | 2026-09-28 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d6c9ff75-7e34-3f9d-a3a1-26afe5b7cf27 | -0.4889 | -49.1327 | 2026-09-28 18:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 89c6026a-6008-365e-9e94-0c11c3ba3c81 | -6.8057 | -45.0474 | 2026-09-28 18:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7f8d2a44-7a78-378e-b317-a799d5a4482a | -11.0223 | -54.1379 | 2026-09-28 18:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.2 |
| cbda5bdd-9126-3a2e-bcc8-75b48b5f3f15 | -5.7386 | -45.0399 | 2026-09-28 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| f8655b95-94f7-3d50-b145-384dc345ca36 | -5.4762 | -45.1262 | 2026-09-28 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 240.1 |
| cec9e212-ea1e-3a90-858d-278e7ddecf30 | -11.983 | -57.6066 | 2026-09-28 18:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |


[Clique aqui para ver as próximas entradas](README176.md)
