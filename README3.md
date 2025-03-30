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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fd4e5f5-c130-3b13-925a-0db0c1356b1f | 4.27684 | -61.32965 | 2025-03-30 05:25:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d5f64f-cb3b-3516-bfc3-8d0b16e90612 | 3.24657 | -60.14951 | 2025-03-30 05:25:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c34bb0f-a5cb-3711-9b06-b960eef3ffe8 | 3.41647 | -60.80574 | 2025-03-30 05:25:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b6584d8-ca32-3701-9c7f-0dfe7b2647ff | 1.83223 | -60.87867 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1818b83c-270d-3bc4-869e-3aa695de1190 | 2.18754 | -61.82241 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b137946-b1f5-341d-8e87-aa624efbe2f9 | 1.15803 | -60.50199 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc9393a-2123-38e7-8bf3-b0e58125ce01 | 1.82669 | -60.88659 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db9eaf3-d72f-3056-86e2-efaad5cd7ed5 | 2.36661 | -61.29509 | 2025-03-30 05:27:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65e65197-504d-39af-ae92-19146c8e1716 | 2.6884 | -60.58576 | 2025-03-30 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61005791-64ce-3664-a069-38b35fb33d19 | 1.02927 | -60.48333 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75107a47-3d78-3bdb-926f-a10825b1da7f | 1.15785 | -60.67404 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35a6ac51-f15b-3186-b5dc-72d91291060a | 2.19036 | -61.8183 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff59df7-9dce-323c-a528-10a1e48e0de5 | 1.82284 | -60.88364 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6905b49-33fd-3e68-ad5d-ee85f9cfe611 | 1.12639 | -59.34351 | 2025-03-30 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41d1ac1e-7b26-3637-b0a6-5c95a5e57f87 | 1.12366 | -60.52495 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00b019a4-ca50-36d6-bae5-afe3c9a2a805 | 0.82524 | -60.59271 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c80b0a9e-aba8-33ce-9040-7907eaff5f23 | 0.76353 | -60.61293 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ea75a6d-06d6-31ce-8e09-fae8a29d6da4 | 1.13083 | -59.35003 | 2025-03-30 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b019e48e-dd8b-302b-932e-308844222186 | 0.82854 | -60.59221 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85bb12e9-e614-336f-80a4-d8125f591d7a | 2.17626 | -61.81672 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f764a97a-14e4-337e-ac8f-f5292bf0bf96 | 2.08244 | -61.26011 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e040d956-47fb-331e-a369-1ebdc2b57bd4 | 1.83277 | -60.88212 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a80f073-6d6e-3374-8ba9-7b60fa98fe91 | 0.828 | -60.58878 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0ec798a-93bc-3b5b-9cf0-ac206780fba0 | 1.04721 | -60.5332 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2152f2f2-2070-35ca-87de-3658a63a3645 | 2.15427 | -61.83115 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4c56a09-15d1-383a-9a75-ae13477c2c7d | 2.01929 | -60.89932 | 2025-03-30 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90c56a6f-1093-39c2-bc70-205e8af0deeb | 2.30539 | -61.78186 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b988419-d163-37ce-9f5e-166b474cec74 | 2.07911 | -61.26061 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7183859-0ee2-3b9b-8483-a1cb4e5bf34f | 1.58253 | -60.67452 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e98a1631-d446-3380-8709-00198eccf924 | 1.11225 | -59.47135 | 2025-03-30 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf856b5b-2513-3237-a4bf-e960a0a7bd8a | 1.02151 | -60.49857 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39aaf5b2-384b-3114-b51f-011efc38668a | 1.2353 | -60.56379 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf6a25c-2a98-3f18-bb4d-8fbe99be9978 | 2.07336 | -60.9613 | 2025-03-30 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2b211c4-5d5b-3964-8ab2-54441350f718 | 2.27495 | -61.22993 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2013b71c-cc32-38ac-a11a-7de071773fc9 | 1.83169 | -60.87522 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b3a52e-3126-385b-bb08-bec09b7f68ab | 1.82615 | -60.88314 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6138c71d-9917-30f0-8a24-6561ad82b83a | -2.95566 | -60.01587 | 2025-03-30 05:27:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beaec4bb-8cae-36f3-a82c-dc9c1812aa88 | 1.02981 | -60.48676 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e450ba-0c9b-3547-a886-69779fb26017 | 2.17288 | -61.81723 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a13a29a-c0b7-34be-a9ab-7ab1e45ee22f | 1.82561 | -60.87969 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e85fec52-77b5-355e-929b-535bf3294240 | 1.75989 | -60.76271 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5509bc55-6f6a-3fc2-8610-9a0abd159c3d | 1.83595 | -60.87802 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a4fb299-4274-31d1-b1e3-c47ccbe5f144 | 2.17682 | -61.82032 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0740b9cc-951b-30a7-a4fa-6042eac07cdc | 2.18979 | -61.81468 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de7b2fb-41bc-34c5-84b9-4c11b3719ccf | 1.02481 | -60.49805 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b03b38e5-4769-3ce4-9892-031efd3b47ca | 1.09806 | -60.59909 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f4f617-9d36-3130-bf79-7a1707415e63 | 1.8223 | -60.8802 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9af0779e-e651-3e9b-b7e3-be6ae9546c27 | 1.12312 | -60.52152 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69598f9a-b706-3879-aeeb-b55e54deb2c0 | 0.8247 | -60.58929 | 2025-03-30 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00a87296-2184-3bc3-b89e-172ea96ff2ec | 1.12419 | -60.52838 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d43ac215-9abf-33da-ac0c-b24cddb23964 | 2.13734 | -61.85598 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8edfa410-57a5-30e8-b17e-467efc4049c0 | 1.83 | -60.88608 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13b0e45e-3e74-3645-b454-63b164fb0ee4 | 2.68563 | -60.58971 | 2025-03-30 05:27:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0567e14-8b31-3c47-8015-4eeef4d214a4 | 1.04667 | -60.52978 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c44c82d-f57f-394e-b3fd-9c8cba1e10b2 | 2.15089 | -61.83165 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 953f10c0-95ee-366d-a4d3-ad5cc23ff007 | 2.1379 | -61.8596 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f0d7814-8617-3a48-a672-c71c53a02f29 | 2.19093 | -61.82192 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c4810d1-fd79-3103-9a2c-cb8ad3964d06 | 1.12694 | -59.34703 | 2025-03-30 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db3250f-66da-3922-b551-08c4f87fa879 | 2.1545 | -61.35275 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cf1186b-7c0d-33e3-9356-51dd7d98d88c | 1.82338 | -60.8871 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c80fa4-a62b-35ed-88fe-86353dfdebd4 | 1.12361 | -59.34755 | 2025-03-30 05:27:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 404a4a94-7ac9-3b0d-ae34-27f624ed8e14 | 2.15371 | -61.82752 | 2025-03-30 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d81a5b7-1827-3cf4-8de5-69e301cf591e | 1.82946 | -60.88263 | 2025-03-30 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1883e393-40a1-37e1-92a6-eef2ed718b77 | 0.82858 | -60.59383 | 2025-03-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 984d2eab-6ea1-3916-a956-bb6f8bed6914 | 1.38481 | -60.80219 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94a33f4b-484c-391a-bf7d-1522e15585fe | 2.07618 | -60.96162 | 2025-03-30 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 848aa4a4-84e5-3e4f-bdbf-f0d5385d59f7 | 1.38906 | -60.80152 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93a32f2a-8d6b-348a-8d40-f7414f8359f0 | 4.27489 | -61.32816 | 2025-03-30 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde39902-2f85-3d25-a494-3c366aa46d0e | 4.27486 | -61.32485 | 2025-03-30 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e74f308-9a27-37be-9601-7eb3936a4db9 | 4.27567 | -61.32989 | 2025-03-30 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143a8d2b-dcc9-32bb-9c5e-2853ce9a8594 | 1.11065 | -59.47336 | 2025-03-30 05:53:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83357580-3176-3fcb-aee4-dc538192d510 | 1.82939 | -60.88194 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b93a54aa-db90-394d-b558-620bbdf72bfa | 2.15398 | -61.82889 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0be8980f-4132-3ff4-82fb-eb8482edf546 | 1.83299 | -60.87742 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64892fef-6460-3b36-853f-842663642dfd | 2.06723 | -60.95918 | 2025-03-30 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 590b1451-5c9f-3284-a1cd-c5c22d066b38 | 0.82359 | -60.5927 | 2025-03-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d19cd769-d804-310a-b7bb-8776e3a77905 | 1.83353 | -60.87834 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b862f1ad-2b2f-3846-ad14-3688f413cc4b | 1.82999 | -60.88576 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41646157-f2d4-3ba6-ae77-500e4424b778 | 1.12301 | -60.52845 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85b86391-f0a3-3924-a965-d21a289ee181 | 2.07201 | -60.96227 | 2025-03-30 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7a9e125-ef42-3328-8c5e-975ef50245de | 1.12283 | -60.52137 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 664eb236-c169-384a-91f9-de8c6d9aa0ac | 1.83059 | -60.88666 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61be76a1-dd1d-376b-a3de-4d1e2a77684f | 2.17676 | -61.82009 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba93bf3f-b66d-3a1a-b805-00a0fc8274dd | 1.82996 | -60.88285 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c409a4e6-d00f-3c06-ab4f-040d571b6f6a | 1.02641 | -60.48376 | 2025-03-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4210e848-4328-32e8-a211-d3f5c40551cc | 2.0714 | -60.95852 | 2025-03-30 05:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9ab13b-0256-3c7a-ac7c-3c30a22acf9b | 1.82458 | -60.87877 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ae03056-cec8-34df-99ae-29a7f2424576 | 1.12736 | -60.52773 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2caed61-d4e6-3f43-8f45-5f41223dd0ad | 1.11533 | -59.47258 | 2025-03-30 05:53:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6713a7de-0b38-3132-845c-f9485ffe0806 | 0.82355 | -60.59036 | 2025-03-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a994e3-08d4-38fe-9fdb-4f70e8936e90 | 2.19249 | -61.8201 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f234c71-77f9-3b49-b585-758084250894 | 1.12419 | -60.52969 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 669f78ff-6e81-33c6-bb0d-3539c61a1daa | 1.82579 | -60.88644 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff21e76-e0c7-3f5b-b28d-0ab0ef7e5a1b | 2.17283 | -61.82072 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7b70f8b-aed4-3c68-8d88-4fa7450cefda | 2.15701 | -61.35344 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54035bf8-d0e6-33b0-872b-786033d31361 | 1.12351 | -60.52554 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bec391f-da09-38e3-b883-7046f6227ebc | 1.83719 | -60.87673 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb60438-7870-31ad-86b1-ff0e211b5a15 | 2.18854 | -61.81813 | 2025-03-30 05:53:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66e20b2f-7a4e-31a4-a5dd-69e1011c6155 | 1.82159 | -60.88711 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d67640f-f601-3b59-bf12-6d0021e1277b | 1.82519 | -60.8826 | 2025-03-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
