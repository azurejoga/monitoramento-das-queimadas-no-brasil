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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef20ddbf-174b-311d-8f20-084e9dc54a49 | -10.6094 | -53.9902 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 64946dbe-5b02-3ebd-a105-eff6daa22f51 | -12.9276 | -51.0076 | 2026-09-22 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6d544912-d011-3c95-8328-e13a85908a3e | -6.9683 | -47.4899 | 2026-09-22 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c495839d-ae51-375a-b9a5-37139320c18e | -13.8957 | -45.4681 | 2026-09-22 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 97d2a687-fc64-3253-bb0c-ecff6218bac7 | -11.8559 | -49.979 | 2026-09-22 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ea50b0e1-9c7e-326a-9f62-d9f845ca9c7a | -12.3297 | -50.1586 | 2026-09-22 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 80f691eb-af86-382f-8826-d2d67307031a | -6.9225 | -42.9088 | 2026-09-22 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 5204e30a-7a2f-3d49-a9dd-12797168fdec | -7.2994 | -59.5343 | 2026-09-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 1241eaee-a8cb-399a-8340-8c8ca2bfca2e | -11.4404 | -47.3355 | 2026-09-22 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 24e3aee2-a169-33c8-b52c-87a269174736 | -11.7076 | -51.0024 | 2026-09-22 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e4d8d53d-dafb-3f70-aaef-b72a69f5cb47 | -6.1651 | -47.5271 | 2026-09-22 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f49f53b8-83d1-35f3-861a-686d94e44f23 | -3.4598 | -59.5591 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3ee63dd2-0b84-3bb6-acb8-6884ff9be7ef | -13.4335 | -46.326 | 2026-09-22 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 224.4 |
| d31dcd48-6970-3888-b6e7-3fdb349dd6b4 | -10.5745 | -46.7521 | 2026-09-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6deabef1-dcb0-3821-b892-76454ab9b14d | -12.6799 | -50.9526 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e5fba713-fd49-36ac-9ed2-91eb9b18e806 | -12.3407 | -50.6728 | 2026-09-22 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 682c2d22-00f5-39b2-97f6-c6ea5639f9ff | -9.2762 | -46.1627 | 2026-09-22 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 19f7249a-5e08-3ed2-be6a-18dbbd48ffa5 | -6.2396 | -41.6634 | 2026-09-22 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 4f3b8acf-c716-32f3-abbf-c18b5bd06a3b | -8.3952 | -47.2784 | 2026-09-22 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e0676143-3599-3138-b0d5-54fdc01f94df | -3.478 | -59.597 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 10470464-c50a-37eb-866b-3584fd99d839 | -6.7989 | -43.9008 | 2026-09-22 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 585fabe7-1592-3c66-850d-b3666e6fd268 | -6.3842 | -55.265 | 2026-09-22 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cdcb6889-d461-3528-a9f1-f8760468f457 | -6.2948 | -47.6274 | 2026-09-22 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3916372c-8de4-3c75-8c96-9c56c1cecd40 | -6.295 | -57.735 | 2026-09-22 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1c60f841-dab8-3f63-8368-948c9449c042 | -12.0839 | -50.0162 | 2026-09-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 2f29afbf-6fde-38e3-9f9c-528c4863a1f4 | -9.5353 | -47.9569 | 2026-09-22 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 159d0c9b-242a-338a-8767-8a802d264b6a | -6.1109 | -57.684 | 2026-09-22 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ba404516-52ef-347a-834d-b1fb07043c88 | -8.6322 | -62.4974 | 2026-09-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 71c00036-dc39-3215-b289-97d28f98fb6f | -10.3126 | -50.5554 | 2026-09-22 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| ef0ac1aa-0141-3c5b-9d73-39da5e025fe1 | -7.1203 | -43.7323 | 2026-09-22 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| c1e2a694-7b05-3f8d-941d-6c648ef00edf | -8.6135 | -62.5171 | 2026-09-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 99ce77b5-ebd9-3620-b0f1-b355458fdebd | -6.1653 | -47.5052 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8e84da1f-d2ca-3b05-81a7-78fb66de5322 | -12.6799 | -50.9526 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 19a21062-04d8-3d66-86fb-51571b646bda | -13.204 | -51.6768 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| bd0640ce-3d17-3b06-8387-b395837ff647 | -5.841 | -53.5205 | 2026-09-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2a138d29-a0fc-38e2-81c9-294e7917c8eb | -12.2827 | -50.7226 | 2026-09-22 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 414ad0fe-c374-31b5-83d6-90654dc90a5c | -8.5982 | -54.6341 | 2026-09-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 144db837-3bce-32d1-ac5e-14e1aed82b69 | -12.6796 | -50.974 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c52ece4c-e937-3d05-b7e4-c85f02ad42cd | -11.4213 | -47.338 | 2026-09-22 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 93627500-ac7d-397c-b95a-a2e8d93c09a6 | -9.0475 | -44.9166 | 2026-09-22 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 9a2aef74-83ed-3b23-bdf5-9356f33ccb0c | -9.5356 | -47.9349 | 2026-09-22 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f2f56f16-b766-30a9-bd12-654e091f03ba | -5.7873 | -43.7758 | 2026-09-22 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b1a41d7f-1d49-3fc3-8be1-a4e31defb8d4 | -6.2761 | -47.6287 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 77fc4ff1-dd52-3304-9655-ba40af582d8e | -8.7916 | -44.2778 | 2026-09-22 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 4e1c57ca-e1d8-36ac-aad7-17f346749c7c | -12.6608 | -50.9549 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b642e612-57cb-3409-b58b-c2ba7ac1d8bb | -11.5116 | -45.3581 | 2026-09-22 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 293f33c3-6ab2-32df-8981-4ce55cf18ef4 | -9.5668 | -48.435 | 2026-09-22 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 739a1619-623a-31a8-a1de-eba2c984a4be | -8.5984 | -54.6139 | 2026-09-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| cd757f82-8074-36bf-923c-5da85a2e577e | -3.3867 | -59.5223 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| f7bfc29d-bdbf-3d42-bd48-4353e434713e | -9.7883 | -46.0593 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 23670880-f670-3346-bb36-8287c89797d6 | -12.0836 | -50.0378 | 2026-09-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 6de4537e-af1d-32fe-bc89-79fe4cd2d9c2 | -8.4797 | -57.6282 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 817ccc8f-3bc2-3ae7-aca9-407b75d7a36a | -6.9414 | -42.907 | 2026-09-22 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| cc1c1c6c-61f3-3412-a07c-72f5a1e0cd49 | -10.0295 | -52.0991 | 2026-09-22 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 6f703738-f704-363d-8b85-b32791dca956 | -9.6108 | -43.9477 | 2026-09-22 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 2187902c-ac1e-34f5-b59a-e227ff67d682 | -9.84 | -46.4136 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f35904c6-22d5-3bfb-9d68-7769f3196702 | -3.4598 | -59.5591 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7751526c-9326-3fb1-b78f-c4aa2e71d522 | -9.7693 | -46.0615 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 42821e04-15c5-3359-923b-014df2bf48c4 | -11.44 | -47.3579 | 2026-09-22 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 06d47c4a-516f-38b8-8a1f-131a08b31710 | -6.1651 | -47.5271 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a33d51b7-356e-3331-a7cb-6639e3d2d43b | -12.8 | -44.2073 | 2026-09-22 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3e3610b7-980e-3303-aa73-3815cc07a9e6 | -6.8152 | -47.8735 | 2026-09-22 14:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b218520b-e1f9-3f13-b06f-8bfc0e3e53be | -6.3135 | -57.7342 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 569a3dac-8324-380f-bdc3-780cb893fc16 | -6.1109 | -57.684 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 52f3b49c-cafc-32f5-b65f-acc5575269b2 | -9.788 | -46.0819 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c35cc618-874b-3c5d-acf9-46606114dcdc | -12.853 | -50.8885 | 2026-09-22 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 56f8369d-a150-3bf1-9215-82d091775486 | -6.3436 | -55.8243 | 2026-09-22 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 35c490c5-77e3-34b2-90cb-33c3af91865d | -8.6507 | -62.4966 | 2026-09-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c951eb43-c8fb-3a90-9d8b-e5f147e072c3 | -8.3903 | -47.6972 | 2026-09-22 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 8519b64a-6b7a-3a5d-a34e-c5fe8e9da183 | -6.295 | -57.735 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 52899a82-59d5-3a34-8c1d-f1dcf3d151a6 | -12.3484 | -50.1779 | 2026-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 06279564-f29e-3315-8aa9-d58799268144 | -9.0286 | -44.9187 | 2026-09-22 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f7602f98-b026-378e-ab15-7ed304d3a8ed | -9.9058 | -48.4867 | 2026-09-22 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 26ad128f-2bb1-3918-8057-ebd92afb81b2 | -7.4765 | -45.4872 | 2026-09-22 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 26d12a4a-43c1-390c-a2fc-c40b33171ae4 | -3.7673 | -60.7339 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 640307a2-74e0-3b4b-a3a7-8a4d182062c5 | -12.6991 | -50.9503 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b36129a7-88cf-3568-9c9a-acdd0fc3c3f5 | -3.2817 | -57.8685 | 2026-09-22 14:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 21994647-1a47-3f92-ae8e-8b1f034d8780 | -8.8105 | -44.2757 | 2026-09-22 14:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 25c86060-9741-3d16-af9d-6955a02a2f38 | -8.7703 | -45.8793 | 2026-09-22 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 974c2f8b-efcd-32b7-93df-811d14fb3c8f | -9.2762 | -46.1627 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 8a8b02f4-d61f-3fb1-a022-055408a93a14 | -9.2759 | -46.1852 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 7a2bf0c8-dbbc-3f45-954b-b35dc441f7d6 | -7.5247 | -46.2252 | 2026-09-22 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 21b644b7-916c-30bb-a85f-652be3708fb4 | -3.7856 | -60.7335 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 204.6 |
| 85927d95-2a81-39ae-8320-f6409cb355ed | -11.4209 | -47.3603 | 2026-09-22 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ee3138f3-7ecf-3347-8f02-3a8640154b59 | -5.6005 | -48.2383 | 2026-09-22 14:00:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 818355b9-9c67-35b4-9f80-51bfa949fa1f | -7.2673 | -44.043 | 2026-09-22 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 5952d86c-1c0e-3b48-a4e1-86533163b434 | -3.3001 | -57.8487 | 2026-09-22 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 413c0c11-7d68-3761-be3d-ffba1ab20264 | -5.5717 | -42.7414 | 2026-09-22 14:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 5123f74c-82be-3748-9bfe-c2df0762c7e0 | -3.4599 | -59.54 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 99ab465c-6690-304d-808f-97d1e50b5b5c | -3.4781 | -59.5588 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| feb198ec-b8a0-3365-a9dc-95cca45b1f93 | -3.6033 | -60.5664 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 278c6c76-d1f9-3740-a283-86b225f89eec | -3.2396 | -53.9417 | 2026-09-22 14:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 902d4258-5cbf-3ecd-a002-f8d6858425fe | -12.1458 | -47.3974 | 2026-09-22 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a2e66fa2-3cb3-3e04-9120-10cc99edc29f | -11.3925 | -46.7598 | 2026-09-22 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| e9cbc551-0958-313f-9dbb-01272060965d | -3.5654 | -43.4727 | 2026-09-22 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2e0a7d0f-0059-3006-b9ec-d0736fe8131f | -8.1872 | -54.7622 | 2026-09-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| edc72d02-b1f9-3ec7-abcb-a9ff76895cac | -6.3842 | -55.265 | 2026-09-22 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9aae925c-595a-326e-a4d3-ad63bfcd6c09 | -13.2033 | -51.7193 | 2026-09-22 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c07b0512-8253-34a2-96b6-d640b5415c99 | -3.2395 | -53.9618 | 2026-09-22 14:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 203.1 |
| 9aee1d3b-7e40-33ad-9e94-16a95f2e0a42 | -11.6793 | -43.4684 | 2026-09-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.1 |


[Clique aqui para ver as próximas entradas](README133.md)
