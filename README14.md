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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40c015ba-d5ad-3b34-b0b3-78106e15b4c5 | -11.65916 | -58.2636 | 2025-05-23 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7766a388-24f5-3f4f-9ec0-929f1ce3b300 | -12.07346 | -47.34364 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61947968-c984-37c5-a844-26fc55fa5278 | -12.59996 | -48.371 | 2025-05-23 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17036047-b208-35ad-a698-39c2503053e9 | -7.79855 | -46.22077 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468d3583-12f8-3072-a13f-0f2334425a84 | -9.95974 | -49.81508 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13925da3-9f5f-3134-930f-f2d7ce5182c8 | -12.07026 | -47.34321 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9dc86d5-5e30-3de1-89a5-7e86f6dc0a79 | -12.07954 | -47.34823 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52765833-b9ee-3db7-a8b6-648f403a7fbf | -10.65088 | -49.47746 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b59b1665-d86f-36d6-8923-92259f15928c | -11.93506 | -43.93109 | 2025-05-23 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 482a91ed-ff7c-30e1-90d0-1ed0ac40351c | -14.67796 | -45.10967 | 2025-05-23 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1233ac7d-c3ce-303c-b3b4-16d079b21a97 | -10.79167 | -48.83628 | 2025-05-23 04:25:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cca8ab3-ee9a-36de-ad34-06d569b29f4d | -12.40308 | -49.98819 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e26df6c-9452-301c-b61c-bfb8b4e8c4b5 | -15.74463 | -43.48903 | 2025-05-23 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e1fa8fb-e0e1-3256-801c-52b96e453d2c | -9.024 | -47.74731 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68a8095a-ad31-3450-8b79-d1154017132e | -12.2961 | -52.49638 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ca42a2b8-b3d3-3fac-9876-b971e0f3da9b | -13.09802 | -52.28725 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8c5c192-bc88-3cee-a2d4-dcdd8473f0c3 | -14.04347 | -53.38078 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d228f5a4-b9e4-3826-bc9f-78f4b23c882b | -11.97029 | -44.15458 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e60c21f6-787a-3784-9b5b-dce128304fa3 | -11.51325 | -48.55919 | 2025-05-23 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7f7254a-8318-37d2-8e95-1024e0c0b6a9 | -11.97331 | -44.15942 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9982eb52-770d-3747-af87-f50cf7c0e9ec | -11.29353 | -53.98292 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 130ef889-9dd8-3a0b-a8b7-46112518c87b | -8.433 | -46.63478 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 396e0285-d841-396f-96a2-dc649c469f56 | -10.36749 | -57.5072 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41bb467d-58b0-3564-a74b-2c0d588e1f2e | -10.49139 | -42.4197 | 2025-05-23 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2a13ac25-73c3-30d9-b3ae-f9394480c6a6 | -9.29283 | -57.55386 | 2025-05-23 04:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a3fa5b3-8268-3cdd-9a8b-0faface782c5 | -12.71995 | -54.97468 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4314b49c-eb50-3bdd-ae1a-585edaa48099 | -12.40618 | -42.52856 | 2025-05-23 04:25:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cc88e086-2cb5-312a-b7e2-53361cdf9a8f | -13.09738 | -52.28461 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fb10837-ef72-3bc1-a66e-40accfdf2485 | -14.87107 | -45.11922 | 2025-05-23 04:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f86ba49-f2e5-3775-bbe7-a82f21aa89f7 | -12.33985 | -49.98135 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a694bb3d-f711-34c0-84ff-8b013f9c024b | -9.21847 | -49.67309 | 2025-05-23 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08e1d10d-dced-3315-a83a-30b0f4aecf61 | -12.27791 | -57.2697 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b123054-9e99-3f29-bff7-9d8d4d2b42d5 | -13.154 | -56.82215 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c4cac5c-c939-381b-a16e-270d4db3dcb4 | -9.02677 | -47.75138 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 253db020-4f02-33ad-bdc9-188320cf2c7e | -10.36826 | -57.50319 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c3c3257-926a-3950-9a6f-065ceebc13e6 | -10.65781 | -49.47863 | 2025-05-23 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f671973-9199-3122-9825-bd793420a822 | -11.29271 | -53.98743 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7666d7c0-390b-3f71-87cd-6a81344bffda | -7.70903 | -45.66312 | 2025-05-23 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30b2c3bb-409c-39c7-99bd-1bfc4a2f044f | -13.94594 | -54.48418 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eedbfd7f-3f86-35e8-ab17-fcf2094eee1c | -9.96395 | -49.81164 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 822756e2-6789-3a11-92d4-9346a2f22456 | -11.784 | -44.285 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| da7ddfd7-9355-357a-aa8c-b1fe1c997fc2 | -14.04007 | -53.37628 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43354e8a-742e-3731-9b14-df5ad25df9ca | -10.52732 | -47.58627 | 2025-05-23 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79369b91-73e1-3320-a59a-ef3e4eecfee5 | -11.29715 | -53.98823 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5051a6a8-12b8-3f88-af9f-ab29415a2407 | -14.04754 | -53.38156 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1dcf90-500f-351d-b65c-8e0317f8321a | -11.08796 | -57.27107 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76dfd7fb-0513-393c-97e8-e43b6319441c | -11.29797 | -53.98372 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b64a989-0dc5-3ba0-b714-2a529d41c17e | -11.30482 | -54.02183 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 211ca161-c815-3809-8360-9903fa7c37a5 | -9.02123 | -47.74324 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f13077e-859b-334e-a88b-00a031cf7b94 | -11.75171 | -47.25227 | 2025-05-23 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6251dac-400b-36bf-99f5-d2a1ea80a8ac | -14.87046 | -45.12344 | 2025-05-23 04:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef5985c4-2c07-3066-9061-36231341acc4 | -8.81396 | -46.65266 | 2025-05-23 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 030ea110-a1f8-3d2a-95d1-02cd50c407b3 | -12.32679 | -49.99526 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8313ec9-4732-3334-95de-1b8048febe5e | -11.55971 | -47.45889 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86affb5e-ee64-3f49-9db9-683137835d25 | -12.39806 | -49.97524 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 310cbb4d-c0f0-3639-817a-c3266a1f4336 | -11.81204 | -57.3555 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5a4c206-c7de-35ab-ad6d-d40b6509cedf | -11.08828 | -57.2748 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26edd46-5c3b-3da1-a78e-a9377906397a | -9.96529 | -49.80358 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e885eb42-8495-3eb8-8b50-b3dd05b44a63 | -13.77838 | -54.3116 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5390494c-84e2-3f1e-a279-7451185f2651 | -12.29494 | -52.49248 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c663d46-4beb-353a-832a-f319a13efbad | -12.72173 | -54.97438 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a9f6538-2ecf-337e-8f81-def4bddd25c4 | -12.84439 | -47.38545 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8af24a1e-57d7-3a09-b20a-18fa4c0e34d0 | -13.59147 | -47.36019 | 2025-05-23 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1f7c759-109f-3f36-a325-d00cd06acb01 | -11.56247 | -47.46293 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e08b0735-75cf-3d79-bae8-8859ace15d5c | -13.15462 | -56.81898 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 103acaa4-6068-366c-8758-36d48e68d66b | -11.80585 | -57.35796 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed4e1c46-8bfb-3e6a-9b36-771f307e910c | -12.32811 | -49.98742 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73215286-bf9e-3d37-9191-384cf0be9ea2 | -12.47264 | -54.47406 | 2025-05-23 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7abc233-d78f-3b22-a50f-7936e2dd85f6 | -12.824 | -47.38559 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac053ae1-0af7-3fed-a698-ce1cd31b49d9 | -9.96327 | -49.81567 | 2025-05-23 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 320e0022-73df-3f8d-8a4f-34fee7655384 | -12.33572 | -49.98467 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cec77756-5e36-305c-b15b-6d0325b37bfc | -12.07082 | -47.33969 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 187a59de-c5df-3398-9925-6d505ce688e5 | -12.34333 | -49.98193 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 278067df-2dfe-3f1d-ab63-9ef666f8e78c | -13.15982 | -56.81991 | 2025-05-23 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ca82e39-395f-30be-a466-1cdd216ff834 | -12.13243 | -54.66021 | 2025-05-23 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d23652d-060a-3d5a-84de-4b589bc54d17 | -11.57003 | -54.56029 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8232f1e-cc99-3e76-b05b-010feed98c03 | -11.78761 | -44.28555 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7bead621-a1ef-3ae0-bef6-60669ef2ba02 | -14.04955 | -53.3704 | 2025-05-23 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63fada5e-fef7-381e-a029-0617a857e48d | -11.55806 | -47.44783 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22f9330c-69d7-3f39-8c5a-d136a987a5e3 | -10.68452 | -57.60455 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78ecb50f-7d92-37be-a0bc-c17fc3650d1c | -12.34268 | -49.98584 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4cff522-172a-3c3b-ba1e-da136445e7fb | -12.33441 | -49.99251 | 2025-05-23 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29a2f652-40ff-34be-b7d6-a38ced312337 | -11.32382 | -58.63096 | 2025-05-23 04:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337585de-564b-3759-9d04-59310b15ec4b | -12.2842 | -52.49421 | 2025-05-23 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bc9ffce-6f01-3ae2-b881-58505089eddb | -11.81134 | -57.35912 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80d0feb8-d1d0-3baa-ba37-6056b0bed4fe | -12.26929 | -47.00292 | 2025-05-23 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5a8c4605-53fd-375e-b81b-bd5b56f2cc09 | -12.07623 | -47.3477 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 100fddae-1933-3255-b38c-f85d7b7ef1d6 | -9.28703 | -57.55267 | 2025-05-23 04:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 46a574d8-d9a7-33b3-94e7-df488ea5c211 | -12.85378 | -47.3906 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07e09526-dbf5-359d-a734-914725666836 | -14.55291 | -48.75753 | 2025-05-23 04:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78d7bfc6-5b3f-3671-b5d3-45aecd7e6f77 | -14.68216 | -45.10603 | 2025-05-23 04:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cd7f517-7d42-3cf1-abf8-c94e9ecaea23 | -11.55861 | -47.44432 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef555175-e214-3b7b-814b-8e78f71c47e1 | -11.56137 | -47.44836 | 2025-05-23 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0865abf8-46de-34cc-a926-f1e30731e4fa | -12.84383 | -47.38898 | 2025-05-23 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30906789-7405-309a-80d5-c6004ad23558 | -10.81913 | -56.95379 | 2025-05-23 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0f27628-58d7-300c-b0f7-3b1d57182198 | -12.2786 | -57.26612 | 2025-05-23 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e14ae2f2-17be-3235-a51a-2a5747d980ee | -12.36138 | -51.38667 | 2025-05-23 04:25:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea5eb02-326f-325c-a0d5-87b27bedc100 | -12.07678 | -47.34418 | 2025-05-23 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95440689-cb8f-318b-ae3e-c4c037cc7bd2 | -11.2988 | -53.97919 | 2025-05-23 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7739ff4d-0764-3bb3-b0e7-816bc6a1500a | -11.78461 | -44.28078 | 2025-05-23 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |


[Clique aqui para ver as próximas entradas](README15.md)
