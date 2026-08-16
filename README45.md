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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d6d490e-ff25-3fdf-bb3b-73ec710212e0 | -13.79747 | -53.80433 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3a9fd0e-654c-3733-bc06-de8af5e3d14d | -16.66879 | -49.13763 | 2026-08-16 05:18:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee8c206-f609-360b-aa31-2bd05d526a01 | -12.74871 | -48.43796 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 137a2cf5-626f-3e3d-945d-2501a5c4e79f | -13.53568 | -46.2487 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0e6dd91-fdbe-3a3c-85ca-7110af684147 | -12.68903 | -48.44626 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b69365b9-1f8e-3432-b8de-e0b3aff62b3c | -14.39728 | -51.87908 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98abad8b-9cb2-315c-929e-0a3d5dcf6b66 | -14.90451 | -46.64739 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4826d05-8ec3-35e1-9aa3-bf55a853fdc0 | -14.44554 | -53.30169 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96e8c77a-dc42-3e0a-aabf-e105d0162c3f | -14.46311 | -51.99752 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abc32027-6f41-3662-a4ee-9492c195e8b7 | -13.70115 | -46.26593 | 2026-08-16 05:18:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bbf9228-bffd-3cb6-94c2-d2916fca19e8 | -17.17823 | -46.11266 | 2026-08-16 05:18:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f591bf6-f464-360a-a693-7da02d05877b | -14.29408 | -51.94794 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cde23841-4f41-35d5-85cf-2d42dee33cb6 | -14.75879 | -56.35566 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c7a2f24-1286-3dc1-b9d2-fcac387e7b52 | -14.48228 | -45.68032 | 2026-08-16 05:18:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5d4e456-eabc-3b97-b9e7-1ef740000ff8 | -18.30694 | -44.51304 | 2026-08-16 05:18:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62d625ad-f9a1-3efa-9a04-1e4e3abb9398 | -14.37704 | -51.90094 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45c39c9b-9847-3e73-bb00-ee0652984b59 | -14.07222 | -53.68459 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b56d0703-e033-3b55-a2d8-4a387fac6b02 | -14.74325 | -49.24959 | 2026-08-16 05:18:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5940103e-5402-3d12-95d1-ceebe366d937 | -14.39673 | -51.88314 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0eafb133-5c94-300c-a0e6-188b3909284f | -15.69956 | -47.62793 | 2026-08-16 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 450b98ab-20d2-35a3-9e05-915c608418f2 | -18.31407 | -44.51382 | 2026-08-16 05:18:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 058714fb-3584-3381-92fb-d6e2de79858c | -13.69073 | -46.24826 | 2026-08-16 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b059c58-c905-33f9-9b82-7c4b5e23909d | -13.68408 | -46.25222 | 2026-08-16 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c238f6-2720-3949-91dd-666bdb1f1a18 | -15.06927 | -47.01421 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 093b1d06-85f1-3929-86c8-5b14275cfffb | -14.89841 | -46.64697 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 270d0da7-94bb-347a-9393-7c2b57ad44a1 | -14.44166 | -53.30114 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9300a415-e2e5-362e-9322-9672c14f7eab | -12.74874 | -48.43793 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b51c88b1-4bc9-30c3-b7d0-2ba5f91a75b2 | -13.91522 | -53.945 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65f7b0b7-a82c-3bbf-936f-af508d2779dd | -14.38397 | -51.88133 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56161b20-feb1-3855-9c32-fc6f014a8d55 | -16.88731 | -54.16032 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdbc78ed-b76b-3c16-a8c7-2fd60ad50671 | -14.75372 | -56.34336 | 2026-08-16 05:18:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5021003-c3ef-35d8-a82f-da7f910f32a9 | -14.38877 | -51.87788 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb286f3b-6713-391b-ae35-169b1231850c | -12.3976 | -55.76658 | 2026-08-16 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 491901d5-7f3d-304a-a101-4bb8dbe370bd | -13.25808 | -51.67993 | 2026-08-16 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f220e35-0b3f-3ccb-b7da-c912f5d270f8 | -14.04464 | -53.66129 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea70363d-b264-31c9-ba9f-f11893fba732 | -15.22635 | -57.65176 | 2026-08-16 05:18:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 537f05ff-c6e7-3f73-9c75-f51efd12ff7b | -13.50268 | -48.23496 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab2797e4-46ab-348c-aee0-511b11289890 | -14.30831 | -53.05753 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1bc1065-24bf-3967-9313-90923fddb025 | -14.06844 | -53.68401 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9064bbc8-ff87-336c-8a54-f60a3c69a263 | -14.37758 | -51.8969 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f66b2209-3e54-35e5-ae98-6fd9f4228fde | -14.71854 | -52.88758 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff4e132f-b9db-3e36-9acf-72415fa36f23 | -16.89111 | -54.16096 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaea0d12-2601-3255-990b-12e2bf4819b9 | -13.70624 | -51.8828 | 2026-08-16 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c768c8f-2f6c-340e-ab56-1d57e4103a0a | -15.06877 | -47.01877 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 87e087b1-61de-3fac-8548-bd1dee185d68 | -12.69075 | -48.47513 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a850d6-bf0d-334e-9287-d28505106e63 | -14.41092 | -51.93853 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91de2c30-a77e-3e2b-b409-fea37df7fb06 | -13.8164 | -53.77897 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87aaacbd-52e1-302c-8cc0-6b095fd07d7b | -15.7053 | -47.62878 | 2026-08-16 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c085996-7d92-3986-9559-ed758b65427a | -12.68633 | -48.46796 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c377f277-3f42-3e56-a20f-fbfd5e69b37a | -9.50744 | -68.50159 | 2026-08-16 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25cf22db-73c3-3bcb-9d42-6f507eb05353 | -12.70114 | -48.47711 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ed55eb4-ed88-3512-8e1a-e7e1603b1ed0 | -13.42013 | -57.04995 | 2026-08-16 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504b1f5a-bce3-347d-b923-24b8d69b957f | -12.67302 | -48.44647 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eeb7ee61-a18c-3067-9258-c52c11f22551 | -13.26232 | -51.68055 | 2026-08-16 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83478dfe-a371-37e4-ac3f-86cbd211a134 | -13.49776 | -48.23061 | 2026-08-16 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4769ae62-d713-32bd-9393-35365ecd0908 | -14.39188 | -51.91946 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70f40e25-23b1-3a7d-b814-31cbe58c2e30 | -12.06394 | -58.04549 | 2026-08-16 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eb44449-9c5b-36d9-afde-ff32165807c7 | -14.33211 | -49.17471 | 2026-08-16 05:18:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afd17ab7-28cb-32a1-ac2c-b9f3359f7304 | -15.0997 | -48.71641 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ccdee2-5093-3192-8d9f-73ccb3e12a4e | -12.70596 | -48.48107 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a7b04ee-65da-317b-b099-eb3fac57ef79 | -15.10501 | -48.71714 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc9a9a2c-9d4b-3d1a-a99f-7a3cae6c3f92 | -15.06287 | -47.01777 | 2026-08-16 05:18:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 109b741a-1428-30dc-882e-947d1d818d84 | -13.79632 | -53.78555 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85d512f8-5198-3f4c-9845-9d71533ab340 | -12.7056 | -48.48391 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 022b698d-5d8a-3a1c-8203-3ee696e93d77 | -14.90406 | -46.65144 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 87246339-1858-3095-b5ee-7561da3948bb | -14.385 | -51.90618 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b5dfe46-7da1-3415-b38d-caa890ca86b3 | -13.78303 | -53.82528 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4cb47a4-eaf4-3223-bde4-8ca302c42eff | -15.14874 | -48.62207 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e21db56-db32-3839-9fa4-2f2f6e910aa9 | -10.86642 | -61.9011 | 2026-08-16 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75c6ca83-291e-3b12-ad84-2104c9f28f70 | -14.92607 | -46.61884 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c60d755c-b2b3-36bb-81ec-21e7453d47a8 | -14.37811 | -51.89286 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 595b1623-e236-3532-9829-99470f2f38fb | -12.68673 | -48.46475 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd26e41c-8023-3a07-89cd-3622d61adbdb | -14.41037 | -51.94256 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d13e567e-3cc4-3566-9aac-79364df6910a | -12.69557 | -48.47916 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf8075c9-6640-32ac-a6ba-ac369bb66009 | -14.10788 | -54.51549 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7940afbd-5f5f-3667-8998-9048cd000b44 | -14.29974 | -53.06145 | 2026-08-16 05:18:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df7b7835-58cb-3b89-bcac-658ed145bce7 | -16.92784 | -54.13864 | 2026-08-16 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7c0e242-f342-32da-b34e-5cf791b6e8ae | -17.1777 | -46.1181 | 2026-08-16 05:18:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8e864fe0-6ea6-35c9-84d7-da01770dd5c0 | -15.14873 | -48.66764 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6448bec4-7097-3162-b524-f78fee682dca | -15.14347 | -48.62076 | 2026-08-16 05:18:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e213286-0541-3924-877d-00b0d5fd14de | -14.38075 | -51.90558 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb02e623-0a08-3b47-9d2a-0cdf4d50acc5 | -14.21318 | -51.8148 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f652f6de-1b12-3753-b498-30a9b69c3a90 | -14.41352 | -51.95116 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35b0ec8d-faca-35b0-b866-12178424644e | -14.90571 | -46.6363 | 2026-08-16 05:18:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91a191dd-7ab4-3b78-a2b0-a85d6db18671 | -15.69953 | -47.62603 | 2026-08-16 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffbcdf10-9497-3374-95fb-5e631d4780a2 | -14.48507 | -54.02642 | 2026-08-16 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8040d3dd-e389-33b0-9541-19e3decc5767 | -14.77781 | -56.95554 | 2026-08-16 05:18:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b6b747f-f548-3aeb-bc5d-e966d71097fa | -15.27158 | -56.1216 | 2026-08-16 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4409483b-137a-3393-a0de-e14c146bf50f | -15.64114 | -56.14732 | 2026-08-16 05:18:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 315e30a0-50d5-344e-b5e3-bc5687a160ac | -12.67259 | -48.44994 | 2026-08-16 05:18:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d59e085-2339-3e91-88a8-25b00d412fee | -14.38183 | -51.89751 | 2026-08-16 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d037ad2b-46c6-30d4-80b6-6d43241db210 | -13.44026 | -43.85032 | 2026-08-16 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 798dfe51-329f-3d09-8759-de9a1b5a0633 | -6.3137 | -43.6178 | 2026-08-16 05:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 88497d8b-252a-342b-a782-1cfcbec67816 | -8.4275 | -62.676 | 2026-08-16 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dec768dc-55ce-3f0a-bcc2-092530f31ebe | -8.9787 | -60.5156 | 2026-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| c5f8b2cc-5899-35b4-bfa4-de5ba727778c | -6.1107 | -57.723 | 2026-08-16 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a02ad668-ec74-307b-b30b-da0b071d9ed9 | -12.7017 | -48.4753 | 2026-08-16 05:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 79b792b0-79b2-31a3-bdc9-d64080d450fa | -6.1108 | -57.7035 | 2026-08-16 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 53d01e57-fa01-33f9-bf78-53b69dbda5aa | -8.96 | -60.5358 | 2026-08-16 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 982ffb15-a2f5-34a4-b28f-33337ea609f3 | -12.0095 | -46.4271 | 2026-08-16 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |


[Clique aqui para ver as próximas entradas](README46.md)
