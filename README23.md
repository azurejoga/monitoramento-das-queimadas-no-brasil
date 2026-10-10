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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33594aed-28c0-3eb8-8e24-ff243e061155 | -7.5162 | -45.3024 | 2026-10-10 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ae3093d4-cecb-3ec0-8eb1-2bbc829b116a | -7.2471 | -44.1604 | 2026-10-10 02:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 374ff747-96e4-302e-ae0b-86ecbe3674e1 | -3.2571 | -54.1824 | 2026-10-10 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| a7b31865-bd5d-31ef-aaee-e1b478a606f5 | -3.2203 | -49.4417 | 2026-10-10 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 6491635a-3416-3eff-9ac3-04dcdeebd65e | 2.727 | -60.2586 | 2026-10-10 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| abeca4b3-2241-3417-8c84-1a47d580a7b2 | -7.535 | -45.3006 | 2026-10-10 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 47cce657-edca-39a8-b6c7-df35831a90f9 | -10.6199 | -60.4852 | 2026-10-10 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c8fad2be-510f-3284-9c2b-5e94b3ca5247 | -5.7565 | -45.1293 | 2026-10-10 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 97871b7e-b953-3540-be8e-2b5c11af4171 | -6.9319 | -59.2412 | 2026-10-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ad17e1bc-b748-3509-ad38-cfb0a521798a | -10.601 | -60.5056 | 2026-10-10 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 072391af-2682-3d6c-9fdc-9afe2c15467d | -10.6012 | -60.4863 | 2026-10-10 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 576604b7-7c83-3320-a67a-202a2257de6a | -3.7376 | -58.4965 | 2026-10-10 02:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| fa003754-3355-3ce1-8e58-ed25d2733daa | -6.4411 | -55.0424 | 2026-10-10 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2e1614e0-8e5f-38c9-acb1-b3d789765d40 | -3.1285 | -54.1657 | 2026-10-10 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d0be772f-6075-3b48-b9ef-6a2156f2966e | -4.5929 | -55.7168 | 2026-10-10 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3dbd2fc2-6d81-3ac0-a357-97f6ef0bdec4 | -10.9097 | -44.8206 | 2026-10-10 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 8bd49524-8881-30cd-8eaf-366a1c0d7284 | -7.5159 | -45.3251 | 2026-10-10 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 57bbaa38-1847-309e-bac1-986349f545c2 | -7.5347 | -45.3233 | 2026-10-10 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 92a8bc74-b66d-32b7-9be4-8474d1997101 | -6.9318 | -59.2605 | 2026-10-10 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| cc0a9203-7ba4-3da9-bc1e-8455cf8f074f | -3.5676 | -54.6946 | 2026-10-10 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 89b2267d-de28-390b-9c5a-e1cc0a8661f3 | -3.839 | -55.7997 | 2026-10-10 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d15fb887-dea7-3113-a27a-1a6e6207611b | -10.8905 | -44.8232 | 2026-10-10 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2da1f532-d90f-3105-acea-07253079623e | -10.8902 | -44.8464 | 2026-10-10 02:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d09ccf17-6eaf-3336-a6a8-f2113a3825d5 | -10.1811 | -36.2691 | 2026-10-10 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 50.7 |
| 01c51806-516a-398f-9b14-49acb4515593 | -7.0228 | -47.661 | 2026-10-10 02:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 531dcfa7-4580-3306-8786-be4aedba1464 | -10.1806 | -36.2962 | 2026-10-10 02:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| 0e1a4366-e5fd-37d8-93b0-8e1eea36078f | -3.2203 | -49.4417 | 2026-10-10 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 6a054326-c7b8-346a-acc4-6d00cd6b2a40 | -7.5162 | -45.3024 | 2026-10-10 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5bce03e8-ee3d-3c37-bea4-aedc9020e852 | -11.0933 | -44.1209 | 2026-10-10 02:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7ffb40ce-7856-31ec-8d94-916554cbfaa7 | -3.1284 | -54.1857 | 2026-10-10 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5600663b-7ee4-3764-b8e6-95b164d08c3e | -18.9222 | -47.9105 | 2026-10-10 02:30:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 63f57e34-7111-3b2d-acec-4e2a08467fc4 | -7.927 | -54.7384 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 12c04d2a-3ce5-39d0-ac6b-3a89c0728d94 | -7.5347 | -45.3233 | 2026-10-10 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 302d5adf-1747-3bbf-ae82-9063c7ea6a1c | -7.5687 | -64.585 | 2026-10-10 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| ce9099fe-1740-33c9-b085-358123623ac7 | -7.535 | -45.3006 | 2026-10-10 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a6fb325f-ab37-31ec-89a8-035cb84d384b | -3.4421 | -59.3681 | 2026-10-10 02:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 0e729749-abe9-3776-91f9-e7307918db53 | -7.5159 | -45.3251 | 2026-10-10 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c8e5fca3-0798-3cde-9829-37101279e480 | -7.9272 | -54.7182 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e7d48869-1f4b-3bee-877f-3003d12040ce | -10.9953 | -45.4068 | 2026-10-10 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9b6a6824-a120-3e55-a747-013d6523ec14 | -3.6048 | -54.5936 | 2026-10-10 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 7defbe53-61b2-37d1-8122-77cc4767f5aa | -3.7494 | -60.6014 | 2026-10-10 02:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2fae2d35-ea35-3e82-afa9-1dfa482aeade | -6.4566 | -55.5008 | 2026-10-10 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| eb67e40c-36fb-3ef0-98a6-c5ad7bc163fe | -10.8905 | -44.8232 | 2026-10-10 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 75c0fde7-fc31-3f4a-8a09-744fe6ee02a7 | -9.9384 | -44.8791 | 2026-10-10 02:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d173a62c-d958-3d89-96e2-ef83215c4748 | -4.4025 | -49.7774 | 2026-10-10 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 71968c23-3a09-3bf4-ba81-cd7715fab8e8 | -12.2154 | -57.1287 | 2026-10-10 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| be8f008f-31d6-3a0c-bbf3-cea98651c3fd | -3.3129 | -54.0001 | 2026-10-10 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9fcd13e7-0329-3fc2-b23e-09381d6fd40f | -3.2031 | -53.8621 | 2026-10-10 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 53d6c8ba-43e2-3201-9a75-4ad8389dc1f6 | -3.2204 | -49.4205 | 2026-10-10 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8949efdd-1ffe-3899-828b-13e0ef5c90cf | -3.5864 | -54.5942 | 2026-10-10 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fdd31b3e-0d96-3d86-87ae-2f0e1dc4b3ff | -10.9093 | -44.8438 | 2026-10-10 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e3fa6486-2ad2-3f82-bfcc-dad8382a69c9 | -5.7565 | -45.1293 | 2026-10-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3853e2e8-cfab-3fef-a3ab-028d1b5df3e7 | -3.9911 | -59.3752 | 2026-10-10 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dcdc2169-6e8c-3f11-9bcd-a812ad289e86 | -7.4975 | -55.0055 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7a438def-6f98-3bd3-9c08-69d16505c9d0 | -3.839 | -55.7997 | 2026-10-10 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6f09a1d3-82dc-3a63-837e-75ac0ef33e7d | -5.7378 | -45.1307 | 2026-10-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e0d4f82c-4061-384f-9860-cf544f7cfd6f | -3.5676 | -54.6946 | 2026-10-10 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6138dbfa-0166-3c80-a6ac-f723d99aa6c5 | -11.0144 | -45.4042 | 2026-10-10 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c41291cd-47ca-34b2-89ec-162a7d68b434 | -14.4535 | -43.9359 | 2026-10-10 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 0e99246c-c7db-3867-a6af-55093cc9e55b | -11.014 | -45.4272 | 2026-10-10 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c7fdff69-ca34-38ef-81ed-7686890a427d | -3.9912 | -59.356 | 2026-10-10 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2066c175-27a5-3c06-9573-87caa9fed031 | -14.453 | -43.9598 | 2026-10-10 02:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 38601e7a-212f-341b-b450-dece65cc5df4 | -6.9318 | -59.2605 | 2026-10-10 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b26d9c96-28c1-30b6-ba7a-4660dd85c98f | -6.4411 | -55.0424 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 02f83b45-81f7-3e36-8030-82700348550d | -4.5929 | -55.7168 | 2026-10-10 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 376cf480-69c1-3cfc-af96-06128ab4d875 | -12.2877 | -63.3711 | 2026-10-10 02:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fb9c143b-945f-352f-a080-e74a36ecdde7 | -10.9097 | -44.8206 | 2026-10-10 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 2d5efcc8-a577-3c19-9c9f-d1de827bb9dc | -7.9086 | -54.7194 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 5a1b308d-c9e1-3029-bc0b-5629b7881118 | -3.2388 | -49.4411 | 2026-10-10 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1cc1da6a-42ad-381c-a0dc-3bfa06254214 | 2.727 | -60.2586 | 2026-10-10 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1811095e-721e-3928-b92a-c5faee51835c | -3.1285 | -54.1657 | 2026-10-10 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| bef2dc8e-a724-3e50-9935-29ef2adf7191 | -7.9084 | -54.7396 | 2026-10-10 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 0b183c29-fb71-3dbe-bd42-45e6934a05a3 | -7.9272 | -54.7182 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 516f8140-6837-31e5-a87b-893260662322 | -7.9086 | -54.7194 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bd94e491-61e1-3384-9078-a47735f53fb8 | -4.5929 | -55.7366 | 2026-10-10 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e2b0e1fb-b5da-379d-b862-5c202d92e53b | -5.7378 | -45.1307 | 2026-10-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 91cfbec0-5574-3994-90f8-f6929c8b02d9 | -7.927 | -54.7384 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 60bcdc47-2502-38e8-b403-fcab0fd3fa55 | -4.4025 | -49.7774 | 2026-10-10 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 4d53fcef-76f6-37f3-b6f9-422197fac78d | -8.6883 | -62.4002 | 2026-10-10 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| e352a549-384f-38ac-b589-32d8ed62d0c2 | -7.5159 | -45.3251 | 2026-10-10 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7dd6ec34-98ee-3854-8497-83a508ad2b61 | -10.8905 | -44.8232 | 2026-10-10 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8512be79-eea4-3c20-9a7e-6984870f4eca | -9.9384 | -44.8791 | 2026-10-10 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 72563dba-4cc9-3bba-8d67-6051e7bea3bd | -6.478 | -55.0606 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 28e53b10-aa79-36b9-9b00-e03807640f1b | -6.4411 | -55.0424 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 714617ba-c629-32b7-9a15-127a784643fc | -7.5347 | -45.3233 | 2026-10-10 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c0e01a0d-f880-3160-a840-59e347aec3aa | -3.2388 | -49.4411 | 2026-10-10 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0a55622d-8266-39da-abc0-885e8b572af6 | -6.441 | -55.0624 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| a42385b9-cc91-3ce9-a55f-ca97258789dc | -6.4566 | -55.5008 | 2026-10-10 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9dca41ad-680c-3236-a658-c0c876daa7d3 | -9.9381 | -44.9022 | 2026-10-10 02:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 04078d86-54e4-31a1-a38a-d2b8fce05f5c | -10.9097 | -44.8206 | 2026-10-10 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| f6e74ba4-0c7a-3d2a-88fe-1c780a4c2617 | -3.5676 | -54.6946 | 2026-10-10 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 988189c5-ee38-3524-bd28-c353e80784b2 | -7.535 | -45.3006 | 2026-10-10 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 9de6cfc2-7bda-3b82-bcce-694b6893ffe8 | -7.9084 | -54.7396 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| db6a4bc7-7ecf-3285-a10d-d03f1dada847 | -14.4535 | -43.9359 | 2026-10-10 02:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a2e60986-e246-38ab-9e5a-fbdca65cab32 | -6.4595 | -55.0615 | 2026-10-10 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 0b55b195-db6a-3585-9207-dfa3b6c67a9e | -3.2203 | -49.4417 | 2026-10-10 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| a5f070b4-850a-3316-823a-8fbf5ff1b1d3 | -3.5864 | -54.5942 | 2026-10-10 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 49a6ce58-39fb-3c70-a6f0-3c6980bce8cb | -3.9911 | -59.3752 | 2026-10-10 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 38fb64db-a7c6-3006-b94b-4ddd0926af15 | -10.8909 | -44.8001 | 2026-10-10 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c5d10ab2-647b-3159-a991-6146c46bf789 | -3.7494 | -60.6014 | 2026-10-10 02:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |


[Clique aqui para ver as próximas entradas](README24.md)
