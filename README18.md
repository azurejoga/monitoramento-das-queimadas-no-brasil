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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2b9f35-b9ac-316b-bf12-9bc6acfd6f28 | -9.6494 | -43.90511 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e0a9abc-c999-3c2c-aef2-eb1d91be0614 | -11.33974 | -48.90462 | 2025-11-17 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a25403e-8419-3850-9208-f7958157689f | -3.55324 | -41.99531 | 2025-11-17 03:49:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 200edec4-52e4-3045-9e8b-3a33d07e88c2 | -10.95248 | -48.70803 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 067e43c6-0e06-3376-adf9-de9a2fbfddbd | -11.9565 | -44.94461 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 636244c7-b366-3615-9ba8-1436167579c2 | -13.09898 | -40.03091 | 2025-11-17 03:49:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 00303a7c-eeec-370f-a4c1-5b6f1002d2c6 | -13.22012 | -39.80818 | 2025-11-17 03:49:00 | NOAA-20 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb853c59-f5b2-32b0-9484-8d941b3323ef | -3.83653 | -42.01173 | 2025-11-17 03:49:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d7fdb1f3-9fb7-3f72-b637-4ada8fd78c61 | -8.53064 | -46.07604 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a794c361-b746-358e-bf4b-ea4f1a62cc3a | -9.35276 | -46.60238 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3820f579-cb61-322d-9f4a-f299efed8d40 | -12.40446 | -43.17659 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e6a635b-38c8-3461-88b1-d19fa6fd325d | -10.53515 | -47.91024 | 2025-11-17 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 743350aa-0d05-325a-98da-f3fe6acd5e88 | -12.87308 | -46.05444 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48ae342c-477d-3d66-b610-748ddeed3190 | -12.02571 | -47.01202 | 2025-11-17 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3950c21f-8a56-3a67-a535-10b90ef68569 | -3.81875 | -45.56778 | 2025-11-17 03:49:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 700e2da4-b81c-346d-bcf2-1d767d8896dc | -9.74561 | -43.97504 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b316fe9-b07c-357b-8a6c-81414c6c0526 | -12.8741 | -46.04889 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45f6116d-8ed3-3764-b59c-a925d40aa972 | -12.79854 | -46.44048 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f27ae88-21b7-3a36-ad8f-1bb791c94dc5 | -9.57699 | -49.1154 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51b0d6e7-1592-3b83-885f-8dfe91b11283 | -3.58991 | -43.59806 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b8e203-bae0-3965-8715-178996c2e74d | -12.65732 | -47.16589 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f89eaf68-6686-36f5-ba3c-4423e77ef1af | -11.40864 | -43.32145 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b672d4f6-41bc-3eb3-8da2-86c1aae182f3 | -2.51368 | -47.82648 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bd4e4b1c-2dbf-3d3b-8b22-2f13e5f5ca67 | -9.45681 | -44.86394 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 411ff5d1-fa8e-37b8-807d-04643ccdbfb3 | -10.88433 | -44.63737 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2e0a430-5097-3b46-9626-cd9e0448127a | -10.85255 | -46.76822 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c14a21a-2e40-38cf-a5b3-9b3c6cd3d1a2 | -9.74862 | -43.95782 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51021b81-3050-383e-886b-9021d12dad2f | -11.96169 | -44.94169 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9be5bc4-4877-39e1-ab68-91261a4a5d5c | -2.51133 | -47.83027 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8270c10b-b8c9-366b-b597-1ca0ccaa99fd | -3.66552 | -44.82066 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0919d932-73d1-32e3-bdd3-5303be036840 | -9.85575 | -44.19217 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c389aebc-5d8f-3f7a-8c52-0c36ddce7643 | -13.8179 | -44.46004 | 2025-11-17 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6cb4c31-5da0-3ca7-a329-788643365749 | -11.83937 | -49.2154 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e1e11045-5822-34e5-8912-647537c3757d | -10.96378 | -44.53008 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f974215-0078-3262-a07a-6b7211a838e6 | -12.32998 | -47.77374 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc90a39e-bdaf-3387-8e17-cbd8ac968e96 | -10.85729 | -46.74277 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b84978cb-ead0-3240-beb2-2a73ff177be8 | -3.07332 | -45.20618 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0077d3e6-db6c-3156-8ebe-36d99aee4497 | -3.66082 | -40.94517 | 2025-11-17 03:49:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23866dbb-c781-3ee7-8c75-7d02291da703 | -14.58615 | -45.22334 | 2025-11-17 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f97bf5f-7a14-364a-9039-c41482de96de | -4.20295 | -40.6729 | 2025-11-17 03:49:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ab7a6ccd-9a6e-3c03-85a9-c9de5de4e6c3 | -12.70224 | -46.78064 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2c7cd05-ec66-37b5-bbcd-c2f30b7a58d7 | -12.63302 | -45.07324 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9babbdf6-e15b-3c81-89f5-b5eeb89d1d35 | -9.71928 | -43.97016 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37457211-10ea-33f2-9e9a-b265d4bb6cbd | -12.87041 | -46.4371 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89de9f34-95b6-33cb-99db-2cb548226a9f | -11.425 | -43.32445 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 328b000e-c75e-3bf0-9899-800dcd5f2f16 | -9.33536 | -46.57852 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8acc5c2-095b-3d4f-9134-a047f183106a | -8.33262 | -45.41342 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24f122a9-5d17-3b21-a94f-5f8d93f1d01d | -3.58905 | -43.6032 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fa7710f-c480-3858-b35c-bc191437633d | -11.80652 | -45.30563 | 2025-11-17 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7364fa73-e3a2-320c-9595-2c03e6c95469 | -9.42589 | -44.6427 | 2025-11-17 03:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b6f2058-104f-339e-94ce-8cd5176c3112 | -3.39941 | -44.1811 | 2025-11-17 03:49:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 523e8a32-4cb7-3cb5-998e-1a97df59ba32 | -2.50731 | -47.8254 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c5f8adad-e55d-33c4-b34f-30b890ee06cf | -4.27797 | -44.24332 | 2025-11-17 03:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fa53f39-2bf2-31fa-821e-fffbac2efcf9 | -10.51716 | -40.33084 | 2025-11-17 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5fea70cc-8326-31fa-8c6d-f8f2769aadac | -8.7322 | -48.32755 | 2025-11-17 03:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 340eaa09-c245-3067-bdde-97887bba531d | -12.42665 | -43.1768 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cc04c3d9-bd62-3d62-86c3-6487fc91bc78 | -10.85195 | -46.77139 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f2728a9-0d5d-3e6a-b4a4-e0a3f36e6dd1 | -9.74711 | -43.96643 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e83a3728-e382-38e2-b024-a866c8422b0a | -12.67097 | -47.17838 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53a96ace-9820-31b6-93d1-74b7e6dcf881 | -4.31727 | -38.49013 | 2025-11-17 03:49:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01ed0dd6-9c69-3050-a434-1dc38c1f6ccd | -13.40308 | -43.75276 | 2025-11-17 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e626c944-5285-373f-bb2a-73a2c8c9ac5e | -12.86246 | -46.03097 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3991b0f-faeb-34f3-ac3c-078366860521 | -9.65228 | -43.91452 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e4eb694-289c-3fb1-ab16-606a6a6de2fc | -10.37094 | -44.25192 | 2025-11-17 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 258cc33a-6d05-3744-92cd-81b51d9b5daa | -3.07222 | -45.2001 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b3bff8d-541a-3c1f-a63a-e6f556bb7411 | -11.0522 | -47.61172 | 2025-11-17 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b6e7af-a2c6-34cc-aab9-d6cc26c124df | -11.81337 | -47.58806 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5f129df-e4c7-3803-b082-1278fc7f038a | -3.34711 | -43.49511 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1be4b902-6623-3891-948f-975a49125dd8 | -3.37717 | -46.06672 | 2025-11-17 03:49:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6d01198-f4c3-37a9-88af-f6475e15fb18 | -12.69779 | -46.7766 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7cab11e-449a-3eda-bdd6-6f851577e2da | -9.71052 | -43.96839 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 98f85aa5-aed4-327e-a1f8-971d7f935609 | -9.15037 | -48.0719 | 2025-11-17 03:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6bb6c45-acc5-38de-ac2a-b140a754c27f | -12.86621 | -46.0372 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52818de3-7e50-3bc0-a3ee-644ab3f0f882 | -11.40797 | -43.32516 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 70ed7824-9fee-336b-bef6-c1314e3ce787 | -3.39445 | -44.18027 | 2025-11-17 03:49:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6ebfca3-6cf1-373a-bb9c-296f7b161343 | -11.13641 | -44.93857 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af417b8b-1524-3354-b037-724c7d74efa5 | -3.22026 | -43.36624 | 2025-11-17 03:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d45442-b883-3aa9-a9e9-b5a9cb4db5c2 | -8.32245 | -45.40993 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b7b54ef-9f66-38de-b209-e749434a4a0d | -11.96243 | -44.93767 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de954e65-d473-3e95-941d-db3112f6f482 | -11.40596 | -43.33632 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 146ae95d-1a18-3ec4-91c3-3ee8e49d5f99 | -12.80182 | -46.44095 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f31ee11-f5bd-39cc-8e36-4770bc13de17 | -2.50671 | -47.81861 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 396e6a50-262a-338c-9d74-11158e563fce | -7.96683 | -50.00331 | 2025-11-17 03:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9a02a565-b26b-3cf2-805c-8b0c49bb9777 | -3.60677 | -42.41268 | 2025-11-17 03:49:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff03a13f-2b34-3616-881c-eff22f6a4154 | -7.70141 | -49.39102 | 2025-11-17 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e18f0b9-95bd-3e55-815d-808ea6080d20 | -7.94974 | -46.846 | 2025-11-17 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcf2b000-c41b-322d-a443-f4716d2c2b30 | -9.32485 | -46.57642 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 33f2098b-7667-308c-857d-222280684b91 | -13.96027 | -47.03691 | 2025-11-17 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0c3820e-ace0-3481-bd29-d9046f5915f0 | -7.97347 | -50.0047 | 2025-11-17 03:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76f84261-6080-372a-9306-1ffd275e405c | -11.70131 | -48.85755 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2302be97-bce2-343c-ad50-543e0a8b3f32 | -2.51552 | -47.81582 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da2b828f-ddcc-36ab-9849-452c26bb6983 | -11.81866 | -47.58969 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f42e780b-cab7-3b17-a52c-e10262549e9d | -10.65817 | -49.37881 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 79bd46b2-bba1-3d06-b170-89ba0179ba3b | -4.27306 | -44.2425 | 2025-11-17 03:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9139c49c-0f43-3077-858d-d87c56f53038 | -10.03226 | -44.0682 | 2025-11-17 03:49:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf9fb784-bdea-3b1f-88f7-7d869b90d00f | -12.40096 | -47.59131 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32fef12-325a-3a11-b573-c67b03c5350a | -10.85584 | -44.09469 | 2025-11-17 03:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c010a255-cef2-35fc-a5c2-0aa5961a2e43 | -12.40362 | -47.54924 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7e9b1a8-9dc1-3d4f-a5d1-3bf3b341d89c | -11.83752 | -49.22459 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b1a684c6-83a8-3547-9d45-79ac10e40a3b | -4.2789 | -44.23769 | 2025-11-17 03:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README19.md)
