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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8a70b0c-70f8-3a30-ac2e-8b31e12f3a14 | -1.81808 | -55.28113 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d8513ae-0cf8-31f9-b9a1-c4ef1a70ce2f | -1.81398 | -55.28055 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 915e272e-64a1-3b0e-a1a7-b9267d77c614 | -1.80014 | -55.44871 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a9dd30a-e96e-3b1f-ad5c-e78d90f5ea02 | -1.79956 | -55.45235 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a979f410-4191-36fe-8abc-6f3a18c7af6c | -1.77584 | -55.6581 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43545734-6807-3648-a707-12b7898f0bd6 | -1.77525 | -55.6618 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57dd0a99-2b0e-3e87-9365-4403b3020b43 | -1.75906 | -55.23124 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2abfb6d9-186f-333a-8a51-3eb232bce230 | -1.7551 | -55.23067 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb3904ea-bf4b-3c31-b62b-19a700ce9588 | -1.75499 | -55.23058 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d30e283-dbfc-3864-afdd-e6fb08e6e8f3 | -1.75277 | -55.13841 | 2024-11-03 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a3938c1-0d54-324c-bf27-118e4112e53f | -1.75235 | -55.67058 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f27915dd-d140-3dcd-98df-a659f7489a07 | -1.75222 | -55.14195 | 2024-11-03 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 557eea92-6b9f-3398-8f57-8077ef73fac5 | -1.73623 | -55.19096 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 752e1aa7-d742-3435-b9cd-49ec365f5146 | -1.73216 | -55.19028 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5fe0be3-58d9-3642-8fc9-088cfdc7332c | -1.72685 | -55.03986 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b9fed32-1327-34a1-86b1-3d71b2386d21 | -1.71626 | -55.13273 | 2024-11-03 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b33a50-bf2a-345e-8ed8-4900c1b207bd | -1.71506 | -55.76927 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 976177e1-8521-3779-9f5a-bd3f05cb017b | -1.71082 | -55.76865 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| baf9dc9d-222a-3a3e-bdbc-14fa84b6a153 | -1.68946 | -55.79343 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7614c898-939e-3635-98bf-82667dbab812 | -1.64979 | -55.18398 | 2024-11-03 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82915e91-e308-398a-98f0-d6b75b557497 | -1.61291 | -55.46222 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97ae76c2-e651-3d2b-b7d3-893908e3ad4e | -1.61107 | -55.46119 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfdc90a8-ce2d-3004-a379-d6ac7442f778 | -1.56117 | -55.88866 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b86c968b-705a-34f0-b2b9-d9d2a9ccce8d | -1.55688 | -55.88807 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef3fff0-4c0d-3d93-b77d-208670b620f7 | -1.52988 | -55.41 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e03411ec-10bd-3bf5-a636-fe8704b1309d | -1.51992 | -55.36655 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 175a3fd5-e1ba-39e2-803e-64d6c9f9e0bb | -1.47488 | -55.50268 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75d8f542-9014-33cb-bec0-c013771d62db | -1.47071 | -55.50199 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ef17630-cc80-3fe5-a4f2-9d1c0ca650bb | -1.46051 | -55.78661 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ff6a42b-240f-3623-9563-df6e62cb4293 | -1.45986 | -55.79058 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e735958-430e-3636-8b31-5743f3c9576b | -1.45624 | -55.786 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 060ebc67-3feb-3e50-8476-b06d4a07dd7d | -1.37604 | -55.3333 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8eed88f-d562-312b-a15e-92a1c02d860d | -1.36012 | -55.46186 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b282c71b-8a8e-35b5-81fd-3e0ce9f14386 | -1.35953 | -55.46567 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f971d2f-dffc-3897-9d33-f627b7d10483 | -1.34694 | -55.79083 | 2024-11-03 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86d5055c-5fdc-33a5-9a0d-9f42fab8d4ab | -1.33219 | -55.44945 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59fd4dda-ebb3-39ad-a9cd-0fbe46535519 | -1.29796 | -55.74722 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77af2d12-af0f-380a-8280-43bce0e14aa5 | -1.26608 | -55.70138 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e7a19c2-e820-31e1-944a-b4252d240c98 | -1.26543 | -55.7054 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f886e808-0e9e-322e-9e62-5692259c5047 | -1.2648 | -55.70935 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e73c207-f902-3789-99d4-2da5f98d87e4 | -1.26313 | -55.69269 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e56d9da0-f4d6-3d6a-b415-3e24f5b2601c | -1.26248 | -55.6967 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adb339e0-38bd-3f02-af34-5e187d88fc9d | -1.26183 | -55.70073 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35caf895-72c9-3531-8c76-9ef7166cd996 | -1.26119 | -55.70473 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e14eed2-3254-3200-ba8e-3b3d77b127d1 | -1.26055 | -55.70869 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ed50d5b-f768-3864-973f-1dfc7572ca10 | -1.25953 | -55.68808 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec290e5-1992-39b3-9837-82a13801f141 | -1.25888 | -55.69208 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21b4ba6c-1cc1-3bfa-ba69-a0c490f11cb0 | -1.25823 | -55.69609 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37b0433f-ee1b-3057-b412-9ffc91543786 | -1.25759 | -55.70007 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20329949-8b02-3fe2-b495-7cd206be9e2f | -1.25695 | -55.70403 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc962ed7-c9d6-3249-a9c7-bc9b06210210 | -1.22536 | -55.82582 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 280ca1d2-29ae-3497-bb23-2f3c5bce2763 | -1.22414 | -55.82574 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42f2a149-6612-3402-8d46-b6b247bf3f63 | -1.22349 | -55.8298 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d272d9e9-cc5d-3a65-85ae-30767ae165a6 | -1.22107 | -55.82521 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f5f1a7-cb0a-37ec-a892-38d4e8bbf966 | -1.22044 | -55.82927 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c062da66-d683-3356-aa5a-9c7297f530ab | -1.21982 | -55.83331 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b00791f2-5ffc-3b32-98b9-519c31526ec8 | -1.21919 | -55.82918 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04f5a48a-da88-32ea-a2ea-b40dad6cfcee | -1.21854 | -55.83319 | 2024-11-03 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0dc97f5-ca5c-30b9-9bbd-20d04c5b6ff4 | -3.62694 | -55.45591 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3e58410-749e-377a-9917-f4aef365f334 | -3.6245 | -55.41989 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7659f8d9-cf22-320e-a535-fa4b96182172 | -3.57398 | -55.45131 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f48611-8967-36dd-b1e8-90474202b891 | -3.56 | -55.53626 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ea094c8-ada1-3e2c-810b-8e08b937db1f | -4.30509 | -55.58127 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 646edbde-8fdf-32c0-a440-34892ed4c28f | -4.30384 | -55.57994 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5feeb6ff-c966-3ff7-bc2e-047ed16b1bda | -4.30104 | -55.58081 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42acb349-cfdd-3538-9d07-a5193cd53e4b | -4.2578 | -55.50814 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cf5d220-56dc-3cde-bc8f-eefd666d7228 | -4.25378 | -55.50763 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 076b0da9-287a-32d5-bdaf-3b4296096af5 | -4.2532 | -55.51117 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff186a7-31fc-3247-826e-f2d188133a16 | -4.24163 | -55.86558 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54dc54cd-c87e-38ba-97ec-94f608249c59 | -4.24104 | -55.86926 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27332373-85b7-391e-baab-3c77cebe1f57 | -4.21483 | -55.47005 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34122a3-8735-391e-a6b9-094c4466c0ce | -4.21291 | -55.46944 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4296e642-1d70-3bd7-9401-fa6a974ca80b | -4.18083 | -55.59349 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b49b0c24-e6b6-369b-bc65-265017b0c7ca | -4.18027 | -55.59697 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14e9af63-0deb-3a8e-95e0-33ee50b079a2 | -4.16421 | -55.64565 | 2024-11-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80b9ef0e-95de-3a63-a0b5-bd6ee5b8fb8b | -4.06784 | -55.54344 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 59271fa8-d55b-303c-b573-326a3e243a46 | -3.98755 | -55.73133 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac553b89-7388-3128-9b2b-34e2b40b7bce | -3.93913 | -55.80084 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7bf433c-362a-37d7-9001-2fa04dd35c73 | -3.93326 | -55.78495 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f00a853-6baf-3b17-8a64-6d37bfeaff56 | -3.85913 | -55.98268 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d5bcec7-23c6-34e0-b9a7-3ec2c87c9f57 | -3.79818 | -55.63741 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45c74da0-2291-3b4e-a6e8-2b42e21b50bf | -3.7976 | -55.64096 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27d6d8ed-dda8-3c89-a10a-c09c45c207e8 | -3.79412 | -55.63674 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19749943-b0ac-3b28-af3c-3a00e5d791c4 | -3.7184 | -55.56236 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac60275-c9e2-3c4f-a2a7-2746a7699139 | -3.70916 | -55.56815 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40821dfa-80a9-31ad-83cc-af3341b81bb0 | -3.70511 | -55.56749 | 2024-11-03 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80245a7e-737e-3556-bf15-b65b887ba10f | -4.78984 | -55.70356 | 2024-11-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0635f3b1-a8d3-3ef4-9a68-43a5037f40a0 | -4.78927 | -55.70705 | 2024-11-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5122ffe3-774c-3fcd-9a76-5e6e90ba7b12 | -4.78582 | -55.7029 | 2024-11-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cf163c0-7b12-3509-8d93-5c6e3d6434e6 | -4.78525 | -55.70641 | 2024-11-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83c86235-f532-329b-ae13-00cbe3a64a5b | -4.78138 | -56.03475 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd1bace3-07e1-328b-9ae0-3940709a9a18 | -4.57724 | -55.85556 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e930e4c2-5786-3240-9404-e463bf5d769a | -4.55648 | -55.72632 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35656bf9-332d-3834-aff2-ab5436d1f8e2 | -4.53875 | -56.12241 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc07d41b-e422-374e-b45a-7145bca0dec1 | -4.5382 | -56.12581 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 424f0051-810f-3856-b439-43b50ee9a802 | -4.53765 | -56.12927 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c905076c-40c5-3f97-978d-ba9da385fec0 | -4.53705 | -56.13301 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15c6f727-eff4-325e-91af-bd4f67ba6018 | -4.5365 | -56.1227 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| abab8a08-2acf-36a2-a01c-984968012f27 | -4.53593 | -56.12614 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4b700fcf-0d92-3e44-ac95-c621da94d626 | -4.53534 | -56.12965 | 2024-11-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README61.md)
