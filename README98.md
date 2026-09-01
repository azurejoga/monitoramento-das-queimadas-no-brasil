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
| c9858ab7-fd97-3d88-99f1-c9f1b993f59e | -3.6215 | -60.566 | 2026-09-01 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fb0ef40e-7d47-307d-b578-4fa70a0b59fb | -15.4235 | -52.6836 | 2026-09-01 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 70b67431-c753-37eb-8a08-cc1fb198571d | -7.1786 | -55.4837 | 2026-09-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5fb712eb-25f4-37d0-a066-51e6a07f4daf | -17.1146 | -46.8556 | 2026-09-01 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 183.6 |
| f8654ef0-6383-3c1c-8a20-c8359bb20689 | -8.4235 | -44.9849 | 2026-09-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7c80643e-f998-3b0b-b2a5-9f8365d09230 | -7.182 | -60.6904 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6609ac64-d1f8-3bd5-820b-576d3870ec6d | -8.3857 | -44.9888 | 2026-09-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 85ed674e-b930-31d6-88fc-7ebd551173cb | -10.3577 | -49.9957 | 2026-09-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 231.1 |
| 0a3bc575-b4b7-32d6-b7b6-cce95a98f848 | -14.7112 | -53.578 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ce79b2fb-1342-3cc6-87bf-b513c341435a | -10.358 | -49.9742 | 2026-09-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ad072bb3-4ac3-33a7-86ba-626af50506cf | -11.2439 | -45.3727 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 4a63891b-96ba-3e12-8b94-b5dbc99dbbbf | -14.5021 | -52.2339 | 2026-09-01 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 53f498ce-e277-3cb7-bb79-d654a201775f | -10.8046 | -50.5046 | 2026-09-01 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 206.4 |
| b23923b2-2206-331d-956b-28ff088c6001 | -7.2006 | -60.6706 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 814c73cc-ecca-34c8-84ea-1a9241dce7d5 | -9.9931 | -46.3057 | 2026-09-01 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 3be1e696-96c7-3a05-ba0a-9b67636184f0 | -6.6726 | -59.4445 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 67a3de17-5bc7-30ff-a399-b2dfa3078f0b | -8.9242 | -63.2804 | 2026-09-01 14:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a6276b33-d4c4-3dde-b2cf-440f44d37032 | -11.2295 | -51.2667 | 2026-09-01 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 3e420034-ae67-3c96-b3b0-6763ab91fd38 | -13.0897 | -45.163 | 2026-09-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 93975d2f-7e8e-3205-bc99-43f3110d32b6 | -8.6149 | -54.855 | 2026-09-01 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e5df4541-476c-300b-bee4-af3e2c3b97e0 | -11.2478 | -45.1425 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 68613bf6-d574-35c5-a3da-d4bf3e674c7e | -15.4429 | -52.681 | 2026-09-01 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 5cc1eafb-7138-3223-82c8-052c0ccacee4 | -14.3821 | -52.4827 | 2026-09-01 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3a0fa222-4cc8-33a1-b485-a9b822450cd9 | -11.2673 | -45.1167 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 325cf81b-b85f-3031-8659-e88adcd2e411 | -10.8404 | -50.6499 | 2026-09-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 385f4be9-bf6c-31b2-8a86-52de3b0b9c16 | -3.5161 | -59.0597 | 2026-09-01 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| fb752951-689a-3675-98d1-3992bdb037cc | -9.9912 | -46.4409 | 2026-09-01 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| cda04bce-2fa0-32d4-ae4e-d683a64d3293 | -7.2005 | -60.6897 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2fc77cc7-89ce-3959-84a0-f78b5031cba6 | -7.9797 | -44.2962 | 2026-09-01 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f0fc274b-e1e5-3020-bba2-7db6f6c03fbc | -3.1265 | -61.2377 | 2026-09-01 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 1d1a96a0-7f25-35d8-9f93-4f6841401ed1 | -3.8416 | -44.0824 | 2026-09-01 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cbfcd728-b149-30fb-a2b8-8c7cb10ab861 | -7.571 | -60.4643 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 630ae1e7-7d82-3a72-8613-b5c2c18fce60 | -3.1083 | -61.2191 | 2026-09-01 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 642f1bbd-019e-3eb0-95b0-4e1fdccd23e2 | -10.036 | -44.7056 | 2026-09-01 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 532f9065-6164-341e-998a-9c81dad55c54 | -13.9477 | -54.3971 | 2026-09-01 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0f487e60-de08-37d5-9ba5-8c5641f035eb | -13.4767 | -51.4086 | 2026-09-01 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 68b35842-f197-3d9c-aabf-bab36ac9aabb | -13.3374 | -51.7241 | 2026-09-01 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cc5d5352-60ed-3070-a115-52a66dc20956 | -3.879 | -44.0576 | 2026-09-01 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 16bd5878-a741-37f3-bd79-6bef0eb8982b | -13.0892 | -45.1862 | 2026-09-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4bbe2c7b-1e07-3f42-879c-388e793c2596 | -10.696 | -46.2646 | 2026-09-01 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 349.7 |
| dea1b25d-6c94-30eb-8e1e-0a7033028456 | -14.7302 | -53.5966 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 55d7b56f-a415-307d-9227-a2ed80570058 | -3.1083 | -61.238 | 2026-09-01 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 327d9ca1-e419-3bda-9477-53e5f764f28d | -10.3574 | -50.0171 | 2026-09-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 07c34ae2-dba7-39ce-978b-6e1060fbc672 | -12.1117 | -47.1561 | 2026-09-01 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 27c91075-8166-3d6d-a5df-edab86489a0b | -14.4587 | -52.5151 | 2026-09-01 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 225b00e1-d60d-3f64-a093-81d86e90c9a5 | -10.8624 | -45.3789 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 359.0 |
| 3e715911-810b-3cc2-b113-5cb02bf4d2be | -10.6964 | -46.242 | 2026-09-01 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 2efd8279-ff06-3b28-b8b9-5e4715b543cc | -7.4153 | -44.2599 | 2026-09-01 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1c02f9f0-54a8-3ad8-9da5-6d6e00d35f70 | -6.9552 | -55.635 | 2026-09-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 90473e8f-9006-3638-97b7-64dfbd356da7 | -3.1266 | -61.2188 | 2026-09-01 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f32d4c90-3eab-39d0-9fa4-ab439dda78c6 | -6.1659 | -57.7403 | 2026-09-01 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 59ddac4b-2db0-3a0f-a3f8-d39ff502d2be | -8.4232 | -45.0077 | 2026-09-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 59590346-0512-34bf-8f91-f0255e7334a9 | -3.8605 | -44.0355 | 2026-09-01 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b589a522-fd7d-3035-9d0f-edd855ee44b5 | -11.5479 | -45.4676 | 2026-09-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| c6e864ea-e1e4-361d-afe0-e6f1e28d8bd4 | -5.5649 | -60.193 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 32b78ac2-7b1b-3fa8-94b2-44815e1d5e36 | -7.8443 | -61.1413 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| e8ba86b7-5c85-3fdf-8463-cc58f210358c | -6.6727 | -59.4252 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 148d1b19-c4f2-37c4-af64-a8ade4ce8777 | -12.9589 | -45.944 | 2026-09-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 3fabb028-93ce-36b2-8cf9-d6088dc1ca41 | -10.8407 | -50.6286 | 2026-09-01 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 3901095b-c293-3a8e-bea9-19a881d15f3c | -10.3388 | -49.9977 | 2026-09-01 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 8d255d82-a1cf-3319-a00b-1cbf1e2662df | -11.2317 | -46.1041 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c480b041-62b3-31b5-8d13-ec1c7f47a58d | -8.4046 | -44.9869 | 2026-09-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f08e8dae-52c3-34fb-9d1e-32c13c29e136 | -8.7817 | -46.4623 | 2026-09-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 501.5 |
| 62caf38e-e171-398e-80af-9d4bdc91d1b6 | -13.967 | -54.395 | 2026-09-01 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 767c4bf6-2e89-3286-bba2-20b94806e625 | -9.1429 | -60.9493 | 2026-09-01 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 1b6ea285-078d-396b-ad66-e6e50161d895 | -14.6538 | -53.5433 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 9182be8d-25ff-3927-984f-d30d2f571729 | -8.7819 | -46.4399 | 2026-09-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 381.2 |
| 217fffff-6f3b-3936-b285-fbeba229e101 | -14.6732 | -53.5408 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 6a5e8e08-38ba-3217-972c-d6126ef2e577 | -3.8789 | -44.0805 | 2026-09-01 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 5c4c93b4-7236-3a83-a309-428964291bf8 | -10.7856 | -50.5066 | 2026-09-01 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 1e63c920-db59-3da1-af49-b3fea468894b | -14.6342 | -53.5666 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7f2d0038-77b0-3639-b6fa-ebd22e225304 | -7.3119 | -60.5706 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 342108af-6013-3337-b30f-b83e32ccc80b | -14.6728 | -53.5618 | 2026-09-01 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 06419983-064b-311f-a598-04501ea28169 | -11.2482 | -45.1194 | 2026-09-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5a6bd0ae-cb0e-360f-9d0c-ef595fa43309 | -7.8627 | -61.1596 | 2026-09-01 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 933937c7-1e43-36f8-9f90-c8645d8ecb0c | -17.1345 | -46.8516 | 2026-09-01 14:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 14430a25-c851-366a-9fd7-1588e303ec71 | -7.3487 | -60.5883 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 1b9b41b9-926e-3a95-a772-07541dae7e81 | -6.8009 | -59.5742 | 2026-09-01 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.7 |
| e7a8f828-048f-375d-b287-b7d92e340b39 | -11.6649 | -47.5957 | 2026-09-01 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6ec75de9-ca86-3fc7-bdcd-6eb77d730f6c | -6.6727 | -59.4252 | 2026-09-01 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c88824e4-df27-3c25-89cd-70f4c9619d5b | -7.2005 | -60.6897 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| cf404cf3-34bf-3bd2-ad44-26858fce6bc8 | -11.2474 | -45.1655 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b7bccfaf-aa26-3dea-b0a3-3a94d1f953d6 | -14.478 | -52.5126 | 2026-09-01 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 04e4108c-96f0-34ab-bcc3-ef9d6f2e56f4 | -3.6216 | -60.547 | 2026-09-01 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5b4b06f2-c585-3987-a22f-630dd0b8189a | -15.4429 | -52.681 | 2026-09-01 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 208.8 |
| f64ec260-6f65-3113-9f7f-789a2476946b | -10.3577 | -49.9957 | 2026-09-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 267.3 |
| b7bc4944-6422-3e22-a0e2-ec292eef10d8 | -8.7819 | -46.4399 | 2026-09-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 871e569a-fa3f-39a4-bb4e-721f782a4967 | -7.6505 | -46.7268 | 2026-09-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e095f5a7-7ad7-345c-89aa-2816b3cad4c3 | -9.4339 | -45.6931 | 2026-09-01 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0cf04a2d-1c76-3263-a1de-bb80ef8c7803 | -10.8218 | -50.6306 | 2026-09-01 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 660add67-9666-365e-a5f5-5f6789427f9e | -10.3388 | -49.9977 | 2026-09-01 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8ed90dcc-0860-3f9b-be9f-8b6cd905f891 | -10.7407 | -54.0401 | 2026-09-01 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 94925515-eea7-3a8f-998e-876bc620bf25 | -6.9551 | -55.655 | 2026-09-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a11da7aa-b9b1-3fb8-9ecd-8cf3de1b838d | -10.0101 | -46.4386 | 2026-09-01 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 6d84adba-e132-38af-a64a-05c1a99cb746 | -5.5649 | -60.193 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9e643deb-554f-363a-a790-7fc6e174d782 | -3.5161 | -59.0597 | 2026-09-01 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3ff17d2d-20ad-3e29-8987-4bbfcb5ca349 | -7.2191 | -60.6699 | 2026-09-01 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5b77ddf3-d606-32f2-9dc3-bf891c208966 | -10.8631 | -45.333 | 2026-09-01 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| cf191908-3804-3f4c-a0f2-6c3942fba44c | -6.9553 | -55.6151 | 2026-09-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b2a11694-3c76-37be-9843-28c2a5bc4389 | -15.4033 | -52.7289 | 2026-09-01 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |


[Clique aqui para ver as próximas entradas](README99.md)
