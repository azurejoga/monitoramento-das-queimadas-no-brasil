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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8ee8be5-bab9-3229-bc30-176716492e99 | -7.581 | -44.566 | 2025-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 01a8e74b-0d2b-3132-9222-5eefccddaff0 | -14.9177 | -51.6872 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0fd4efa6-97c9-3085-989a-e3236e9d4d25 | -7.581 | -44.566 | 2025-09-17 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 023894e6-7344-3cf0-bf5b-0b7bae83d043 | -4.0634 | -47.4943 | 2025-09-17 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 266e3e2c-0ce0-3d44-b9bc-dc2564136205 | -4.0449 | -47.4951 | 2025-09-17 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7cef0248-f733-3efb-9d13-f894f643f852 | -14.8207 | -51.7006 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 577a729e-d57e-381f-85cc-30fe3ad7b3c4 | -14.8397 | -51.7194 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c0187d86-8769-3322-b7c8-a5a0956d23d4 | -14.8401 | -51.698 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 227.3 |
| fc9876e1-c417-3481-9475-3fb10fd88ea8 | -6.6808 | -46.2961 | 2025-09-17 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a88c4fb2-b108-37a7-a66c-2fd0ec87d7c7 | -6.6806 | -46.3184 | 2025-09-17 01:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 45dbce4e-06c3-3b0b-bdcb-00ee67b16016 | -14.8211 | -51.6792 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c5713ded-c285-34a2-a9ac-8b6d1c59acbd | -14.8017 | -51.6819 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 835ab94e-40f6-3f25-89dc-9aa4d9d3ec1e | -14.8405 | -51.6765 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ab6e1833-f76d-3431-927c-43497eab530b | -14.9371 | -51.6845 | 2025-09-17 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 13ad5ded-6336-3897-a7ce-3cde65aff850 | -11.0164 | -48.9297 | 2025-09-17 01:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 339a7bfc-2f40-34d0-adb3-e29c3cf6da97 | -15.4192 | -46.144 | 2025-09-17 01:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5607abb1-d182-3d84-a466-2b6ca6deba54 | -4.0633 | -47.5161 | 2025-09-17 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d54ec447-7b73-3c4c-9b65-6ffce218d821 | -17.8728 | -44.4554 | 2025-09-17 01:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 1db47b9a-cb12-386b-85c1-0bd0446c51ef | -9.55908 | -66.73393 | 2025-09-17 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| cb043d7f-40b0-309b-9d9c-e2cc3c8738bf | -10.05614 | -68.45249 | 2025-09-17 01:49:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cfa49bc8-cfc8-3c20-85ef-946d1d994b04 | -9.38089 | -68.77259 | 2025-09-17 01:49:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07a2db57-0e74-3d1d-b1d0-acdf9f491056 | -11.0164 | -48.9297 | 2025-09-17 01:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9997777f-f515-3dad-a60a-64964e1f6193 | -6.6808 | -46.2961 | 2025-09-17 01:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a82425a4-56ec-317e-9161-9bb197539cb8 | -4.0634 | -47.4943 | 2025-09-17 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3eace538-067b-30ae-bfb8-dca9091f7b4d | -14.9371 | -51.6845 | 2025-09-17 01:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9ffe1cdb-ab76-3d95-8d35-40367b45ea5b | -17.8728 | -44.4554 | 2025-09-17 01:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| eb92f3ef-28da-3790-8a33-8f243860c3ce | -14.9177 | -51.6872 | 2025-09-17 01:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| ee887e8e-dfcc-3515-8545-38b9e7927650 | -15.4192 | -46.144 | 2025-09-17 01:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| da1bf125-3306-3851-bd3f-a23a39296e6b | -14.9173 | -51.7087 | 2025-09-17 01:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| dd615f35-160a-31ad-b643-eaacb1c60216 | -8.63305 | -66.70627 | 2025-09-17 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f0c4b497-0826-3dfb-a118-ee0c451090f3 | -8.68826 | -70.13684 | 2025-09-17 01:52:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 802a6af6-7a07-3f1a-a94d-1e6edf7cbffa | -7.64367 | -72.39291 | 2025-09-17 01:52:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 36541904-d9af-3f1b-8fad-19c2caaa9d8d | -14.9177 | -51.6872 | 2025-09-17 02:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 82170e90-f9f5-38db-a038-b1cdb8f63478 | -6.6808 | -46.2961 | 2025-09-17 02:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8154466d-00b5-3ad9-9129-fecc62c6a878 | -10.8215 | -50.6519 | 2025-09-17 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5a8e3781-f033-3e01-a591-c0ef64167777 | -6.1602 | -45.9783 | 2025-09-17 02:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 83b18680-784c-3352-9e47-e340ff6a2b34 | -11.0164 | -48.9297 | 2025-09-17 02:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| aedb4b48-c4c3-3cff-906b-9451b8d4a083 | -10.8025 | -50.6539 | 2025-09-17 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7e9e6f94-4803-3c55-b20d-2ce782f97af2 | -4.0634 | -47.4943 | 2025-09-17 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d14cd8db-b18e-3eca-827b-cf16d940dcab | -5.9179 | -45.9063 | 2025-09-17 02:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f705c615-d289-33d4-afc5-579e93737135 | -5.9366 | -45.905 | 2025-09-17 02:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0b5d48c5-97a3-3737-916c-5a9444c38714 | -6.6808 | -46.2961 | 2025-09-17 02:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| bf4a6ae7-fb00-33a6-b4a4-e07d83aa9a0e | -15.4192 | -46.144 | 2025-09-17 02:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6f536d54-18d4-3f7d-8f7f-0e5224884a45 | -4.0634 | -47.4943 | 2025-09-17 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4bafed8c-d726-3ce3-9c28-db2e961dc13f | -10.8025 | -50.6539 | 2025-09-17 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ee7581c1-ff86-3677-8b0f-45a73200b1ae | -17.8728 | -44.4554 | 2025-09-17 02:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d2816631-1c0d-3b57-9b40-e61dbdc7b386 | -6.6808 | -46.2961 | 2025-09-17 02:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ab263d2a-e609-3756-a582-548c7b74108f | -15.4192 | -46.144 | 2025-09-17 02:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0c75e1b2-6857-3fff-9945-21b910a19156 | -4.0634 | -47.4943 | 2025-09-17 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 994b13c0-30c6-3f08-be3b-ccf52d3d503e | -14.8983 | -51.6899 | 2025-09-17 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d0d5e8b3-35c7-325d-a6ec-ffd2c7b990b6 | -14.9177 | -51.6872 | 2025-09-17 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 297ee708-f398-3b3b-894c-9b5247754801 | -5.9366 | -45.905 | 2025-09-17 02:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 92ddbb0b-2898-3d5f-8165-1d079a0056d3 | -6.6808 | -46.2961 | 2025-09-17 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a4d950a5-c53b-3587-acc3-46ebbe8b8bbf | -15.4192 | -46.144 | 2025-09-17 02:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7eae8307-4330-3fe2-8c7f-4b06f2bbef4b | -14.9371 | -51.6845 | 2025-09-17 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 301bd63e-1963-372e-9572-f6f64db71dcd | -5.9179 | -45.9063 | 2025-09-17 02:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0818ac69-1d13-3c64-a96c-d1301b71be73 | -14.9173 | -51.7087 | 2025-09-17 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 40b19c49-ba22-3bde-b806-3c4c77b69f5c | -14.9173 | -51.7087 | 2025-09-17 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 3dbbd25d-c1eb-3a22-bf0f-4df8f0b4b5ce | -14.8979 | -51.7114 | 2025-09-17 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 5a923df0-9a80-3149-8c54-c5c16f0b639a | -18.326 | -43.3018 | 2025-09-17 02:40:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 80ab2fbe-3d76-3493-b58c-dfcf00f253b3 | -15.4192 | -46.144 | 2025-09-17 02:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 17142028-010a-3bca-98af-e7e4ca978286 | -14.9177 | -51.6872 | 2025-09-17 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| eccaefbb-697e-3813-acdd-1e95b518e1d9 | -12.3865 | -51.4135 | 2025-09-17 02:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 76fe5559-ebdb-34a0-b84b-3c1fbc5f368a | -14.8983 | -51.6899 | 2025-09-17 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 531e9be8-1370-3f20-840e-90da2d341c52 | -5.19321 | -35.86874 | 2025-09-17 02:49:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b61ab6b3-aca0-3dbc-a1b7-d94f06faa009 | -5.18821 | -35.87181 | 2025-09-17 02:49:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 413c3c6a-cb31-342a-8ae0-379162bfe669 | -5.18615 | -35.86757 | 2025-09-17 02:49:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd200f08-e499-38ed-9fc4-d45ecc7d5837 | -19.3172 | -47.432 | 2025-09-17 02:50:00 | GOES-19 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5032c9f2-b9a7-3b4e-9231-6de6bb7b85b4 | -14.5739 | -47.3887 | 2025-09-17 02:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f1c09e3f-68a3-3447-ad2c-85930a0722a2 | -15.72207 | -39.32412 | 2025-09-17 02:53:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cc4a4556-5765-3531-8f2e-2e7713006707 | -15.72031 | -39.32236 | 2025-09-17 02:53:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 110b470f-890d-3d95-84d7-4d4ac057599c | -15.71852 | -39.33025 | 2025-09-17 02:53:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b717a228-9257-3f9c-8031-c920a6e6cf99 | -13.7343 | -48.7701 | 2025-09-17 03:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3f08733d-35bf-33cb-ac3c-7f76b941cae8 | -14.9173 | -51.7087 | 2025-09-17 03:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 00db4982-bf11-310a-8d3b-dbe7a421c97c | -14.8013 | -51.7033 | 2025-09-17 03:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 59b3d4f9-d14a-37e5-bbb4-1ad1d7934b85 | -7.5998 | -44.5642 | 2025-09-17 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7d0f1f4a-7e86-34b7-8940-52a9601b53e8 | -7.581 | -44.566 | 2025-09-17 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6917c619-effe-3141-bd22-507a3254f4d6 | -7.5807 | -44.589 | 2025-09-17 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| a47efeeb-976c-37fa-a282-e0ef6df1235e | -7.5619 | -44.5908 | 2025-09-17 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0a9b21a3-0d47-385d-8f06-166128be3e58 | -7.5996 | -44.5872 | 2025-09-17 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 02b32084-a93f-3f94-a814-dd9563d3ae42 | -14.8983 | -51.6899 | 2025-09-17 03:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7e75ed6c-cc93-30ae-94b5-770214879cd8 | -14.9177 | -51.6872 | 2025-09-17 03:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e686abe3-d0cd-3ed6-b1c4-7a5eee877d4d | -15.4192 | -46.144 | 2025-09-17 03:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8ec1abda-05f0-3f3e-ad92-6cb154b0cb1e | -14.8207 | -51.7006 | 2025-09-17 03:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ac1fdb78-4984-3493-81de-5cc798f474b8 | -12.6922 | -45.8022 | 2025-09-17 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 166d4b98-ec5f-33d9-bead-bcc50e23be41 | -12.6926 | -45.7793 | 2025-09-17 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 70f43a4a-200a-3f9a-8590-353c5113c49c | -14.8013 | -51.7033 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 2d8ab1d4-2d60-3a59-8466-52c03cbdb492 | -14.8207 | -51.7006 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1d81229a-6fef-39d4-b9e5-4930050dfaa0 | -14.9177 | -51.6872 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| ecae778c-41e2-385b-9d1e-2dc0084c3217 | -14.7819 | -51.706 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| efd334e3-93ca-39e9-9388-156c6a9b9f28 | -7.5807 | -44.589 | 2025-09-17 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8f8be411-e0a5-35f4-b99b-3814a9e95810 | -7.8259 | -46.153 | 2025-09-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 13451169-377f-3557-936b-d9f5b16a6ca5 | -14.9173 | -51.7087 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0418c8c3-98a4-3b6b-880f-b79175743127 | -15.4192 | -46.144 | 2025-09-17 03:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d1fa8e91-86fc-3276-ad52-82b2ac07c014 | -12.7115 | -45.7993 | 2025-09-17 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 87bdf8a9-cc3f-3604-b5d2-3d04d13b4bb2 | -14.8983 | -51.6899 | 2025-09-17 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 920d5c35-5e6c-3430-9bd7-699ad6d45d58 | -7.581 | -44.566 | 2025-09-17 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bdb0d1d8-d818-3e6a-a7aa-ac02b4f4dfc7 | -14.8207 | -51.7006 | 2025-09-17 03:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 85ec6bc4-2b8c-3f33-b018-ef9162152c41 | -7.8259 | -46.153 | 2025-09-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e6854a68-8e73-34f5-ae90-16f5c1a1c558 | -9.0432 | -57.0034 | 2025-09-17 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README8.md)
