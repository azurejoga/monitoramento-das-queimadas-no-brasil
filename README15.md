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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b634478-1c1a-3c54-b05f-405e00742c84 | -8.52044 | -44.9687 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71395e18-f43f-3397-ae9a-e70b47a67505 | -5.89143 | -49.6473 | 2025-09-23 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9765bb36-0bcb-3751-b084-bc2eb20f1512 | -7.15648 | -45.00357 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942be719-b7fa-3a64-8f6b-f1c317f3f5be | -11.46464 | -43.52985 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d81bc5-eacf-37ee-b887-101ac65059ec | -1.68879 | -48.19839 | 2025-09-23 04:19:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e6b2e79-82b5-3958-a96c-854b027e10f2 | -9.01714 | -48.03944 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85603013-e022-3736-8d8b-27f8b48f9fb3 | -8.00378 | -45.72049 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d504c2d-dec3-3fca-a434-01df7f87865f | -7.89183 | -44.01721 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2f0f30e-ec36-3709-9ccd-1c27cc552116 | -7.0604 | -45.05189 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46d2346d-c9dd-3133-8a1f-e5c3bffe98e6 | -5.68946 | -51.05407 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19453e2c-dc8c-352a-867a-e44c8f884918 | -11.86068 | -56.87886 | 2025-09-23 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 493372c1-32c4-3105-bcc0-422e4d65146b | -11.01362 | -41.89581 | 2025-09-23 04:19:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0210008a-b260-35a8-b79b-9fe8b3855781 | -7.88296 | -44.03031 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c03c39f7-0811-3a1b-becf-f5a277ca69d0 | -9.58848 | -46.43674 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbbf04e9-c678-304e-9a53-9d284bc1d5d2 | -8.94907 | -44.48562 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c41c7a5-259a-34c1-8e1d-4bc615cf55c2 | -11.82081 | -43.1582 | 2025-09-23 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cbd57728-c2a5-3496-aae4-d94b1f0295ab | -11.86273 | -56.88145 | 2025-09-23 04:19:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b1b7341-378e-3f01-8429-d879e5f00304 | -6.35009 | -56.19835 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a507d0c2-867c-3bd9-bf04-89c6cfd03cd6 | -11.40795 | -44.93399 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d753b9f-322a-30d2-ac0b-a28bfce4948d | -8.34116 | -45.02884 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a67e6c8-8544-3db7-bfdd-d2464666425d | -9.99096 | -46.276 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6205aaa2-d6e9-380e-9ebe-b4cc759d02b5 | -8.54243 | -44.9152 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ef074f2-46a8-3800-9050-b5eaf1c43a50 | -8.80138 | -43.07179 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d4979a5-270f-31a8-8606-7a3ae03cbe1e | -6.33586 | -56.20606 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1581fca8-99cd-39fd-b944-44b2221a5f07 | -7.88739 | -44.02376 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e1a5c7c-5f41-3033-acd6-e95b346efb07 | -6.2509 | -45.33675 | 2025-09-23 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31e2fd29-3f83-3353-9855-214321dc92f2 | -8.09238 | -49.91839 | 2025-09-23 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef7b8a95-8c08-3a19-88f1-5f5a1dcda377 | -8.52265 | -44.97618 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 82e653e3-0b79-3906-acef-a7a2845be795 | -9.19296 | -44.62075 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af09eb08-9b9f-37fc-9b88-31e57aa674a8 | -11.60726 | -45.02748 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bede3b9c-6ffc-35f6-9e71-f9c47e7c303e | -7.89796 | -44.02178 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d34ddd-6758-396c-8862-90382883b157 | -11.99606 | -47.75296 | 2025-09-23 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6402b57-ccc7-3fa1-89c7-46841189fbfb | -7.36477 | -44.54317 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2a957b3-bf54-39a0-89b4-9a422a6c5557 | -7.26475 | -43.00212 | 2025-09-23 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4489fe0-9a0a-38a3-8b2f-d6fc304ec84d | -7.89407 | -44.0248 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90cb8380-37d5-32ce-963c-eb625b30944b | -6.34208 | -56.20716 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c609ec4-b34f-327b-8caf-5225eb73f90a | -11.53096 | -43.62172 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b00fd93a-db6c-3334-8c5c-3e4e0ae6150f | -11.42242 | -44.95077 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c812c7b4-1f83-3e4f-987c-187e2a1e217e | -8.52706 | -44.96975 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d04436d0-39e9-34b1-bd32-dc9e55b78830 | -9.9926 | -46.28709 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5663d2f-ea7a-3d93-a26a-4c8d40084ae1 | -11.45366 | -43.53217 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf15619-d767-3b24-9f95-b07b9c180df8 | -7.16418 | -44.43647 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 930e99ac-d074-364c-a93a-dc8241bd36f1 | -7.87794 | -44.01868 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8738c75-2792-3b6d-b944-8598b00e10d5 | -8.0142 | -45.46436 | 2025-09-23 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc9933da-ab5e-3f9d-8f70-2f728578a94c | -10.35089 | -46.12852 | 2025-09-23 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62ba9b1e-83d8-3205-9fc4-800191a207e7 | -7.89851 | -44.01824 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 556b7a68-d89d-3dd9-a5c8-dc0107614c96 | -6.34117 | -56.21212 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9004144d-ae33-35cc-8820-6689ef1e48a0 | -8.9524 | -44.48613 | 2025-09-23 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 509654a4-e073-3c98-8557-34ee0d3d80f0 | -8.51658 | -44.97166 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3039ec50-7420-3e8c-a695-1cd1aa5831a6 | -7.60147 | -44.44131 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f49b09-2529-3ac5-952b-e60d475447bd | -11.48077 | -43.53124 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fa73d13-1da0-3bd2-bf33-ec4e545bcafb | -11.9179 | -43.42442 | 2025-09-23 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e84943e6-a892-3b53-abc9-a364baad6224 | -8.01585 | -45.45388 | 2025-09-23 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85ce5d3c-1fb8-380a-bcca-4c4ed0db4e36 | -11.4375 | -43.52184 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a4cc108-4a94-3707-ba44-dd2f6d1bf22c | -13.55854 | -42.56067 | 2025-09-23 04:19:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7305126b-dc3a-38d8-ae20-6d09ba0f5db9 | -11.41575 | -44.94974 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25684353-deed-3705-a618-28777c9bbd90 | -11.4398 | -43.53008 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0badab00-482d-3f30-8e88-e1aab200bc10 | -8.3759 | -44.69957 | 2025-09-23 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37c448a3-c778-3ad5-9004-d8f81ba48308 | -6.59305 | -44.54873 | 2025-09-23 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 19c12a4d-5091-38aa-afb7-8b6bf74eb44c | -12.35835 | -44.09618 | 2025-09-23 04:19:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71028883-e847-3789-9525-08626a94223f | -5.92257 | -50.06255 | 2025-09-23 04:19:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da17739c-b526-34be-818b-6befcdbf589d | -9.99592 | -46.28767 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 515d40ac-7105-36e3-8c95-6a2e229712f3 | -11.52577 | -43.63272 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c6101e-9aac-376a-a6c1-ace50c6bffb7 | -11.41739 | -44.93914 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf84c41c-d141-39c5-849e-6ad576ee5869 | -6.33676 | -56.20117 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f909c4ae-c8bf-3770-bef2-737ecd167174 | -7.36754 | -44.54716 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33429f06-b4d8-3d3d-9640-07cff46aae64 | -7.06317 | -45.05588 | 2025-09-23 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f126c65-2f22-342f-ba7d-f16cf5702bb6 | -11.45771 | -43.52882 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bd29f92-1782-3d80-bc0a-4a3f19d9331c | -7.77145 | -44.72125 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 592947e7-722a-368a-98cb-4adc8d28d858 | -7.88685 | -44.0273 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbc46d86-a923-3bb0-a5cf-4ea279ebf043 | -13.56028 | -42.56382 | 2025-09-23 04:19:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33ed5a4d-3455-3194-bf1c-9fb45dde68c4 | -8.51934 | -44.97566 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b85a337b-4cbc-3bce-b12d-3ebbedd17666 | -11.4583 | -43.52495 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ced127b-a0a8-3b34-8c4e-0e6c88f09792 | -11.4981 | -43.55772 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e55ff07-812f-3cc7-ac6b-35e877bf8592 | -11.98405 | -47.65489 | 2025-09-23 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43c260da-e027-302d-9f41-93a71f5560a2 | -7.90185 | -44.01874 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e4a964-c956-3669-9776-e036336b6f25 | -8.01917 | -45.45443 | 2025-09-23 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a091db4f-0979-39b2-ab04-14b7cd929089 | -8.53911 | -44.91468 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a950763-3e28-3b20-a26b-659b5d6c44fa | -11.4802 | -43.53511 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d86699ef-86b8-3eef-8381-fd185ae2542a | -9.29957 | -35.69633 | 2025-09-23 04:19:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5df5f9dd-1a26-312a-8df3-ede89302e2a8 | -6.34477 | -56.19242 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa084ea-b93d-3668-857b-9cc7f1dcf5b0 | -8.5232 | -44.97271 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfb15e7c-5557-3b95-b8fa-be0ffb7c3332 | 0.81399 | -50.69851 | 2025-09-23 04:19:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be66c320-695f-3522-9a78-eec6b0aacfee | -10.65138 | -44.22873 | 2025-09-23 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08912a1d-28b4-3b30-acd5-610c3e8e59df | -11.41461 | -44.93508 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b4b0bb-f911-38d4-8303-900913164a4f | -8.80425 | -43.07606 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d830973f-e7cc-3a24-b31d-905ef1410585 | -10.81742 | -44.80448 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 332eb5bd-d7f5-3658-87b4-0efe6a5c555b | -11.99947 | -47.75354 | 2025-09-23 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ad6bbbd7-f48d-3ea7-b53b-b4d05b606c38 | -11.52809 | -43.61732 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 297e29ab-256f-3ef3-85eb-625c6364dd2f | -6.90646 | -45.57368 | 2025-09-23 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eab2da79-86cf-3bb8-99cb-4cb62a91d774 | -8.51989 | -44.97218 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34f7b829-fab4-3e71-933b-82a44e2dea7c | -8.93935 | -46.72678 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3500dd4b-dc61-3ffb-b2a9-331fef6f3417 | -7.34126 | -39.70803 | 2025-09-23 04:19:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d50c0691-8979-308f-a7e6-2224d48bcdba | -8.14044 | -44.46925 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e44f3452-dbf1-3600-9376-4d6246ac1020 | -6.42257 | -44.16389 | 2025-09-23 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94427885-1d55-32fd-8567-60ffbb5f729c | -7.15703 | -45.00011 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8cb38ee-fc6a-3e9d-aa3a-027e47511680 | -6.34298 | -56.20221 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02067f0a-ce82-3c2d-a41d-01255e4b62eb | -7.04129 | -41.99964 | 2025-09-23 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c0949b33-199b-39a3-8255-c1f4d35a3e03 | -11.82021 | -43.16222 | 2025-09-23 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4f9609d1-a4f2-39db-91e3-023ea0a004be | -9.99648 | -46.28417 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README16.md)
