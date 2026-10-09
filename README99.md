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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe8d75b5-75dc-3d9c-a8fe-53475b0d8f90 | -11.24124 | -44.8716 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 941c1554-ab96-31cc-ade3-a80c290f3bdb | -12.24045 | -57.10527 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d40bdf78-fd42-3857-93fb-5c591e4ce72d | -13.16757 | -54.35636 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 167a0ade-7712-388c-b2a8-ea77a15ec5e6 | -8.90882 | -47.2661 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb3fd8ed-84db-3ac2-8868-c139bcb5871b | -10.73894 | -52.0296 | 2026-10-09 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e90b3f7-d49a-3c8c-82ec-778d2f6c8869 | -11.58855 | -43.64861 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abef5052-903a-394e-93f5-35c079e11cb2 | -13.16677 | -54.36065 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3c771d55-b664-3877-ba00-d495ffbf912d | -5.88796 | -57.72426 | 2026-10-09 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab662559-d696-300d-b8ba-244c89bd9f72 | -11.77772 | -45.54151 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69c7aee1-614d-36ff-ae3b-977073008403 | -8.32396 | -45.45407 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfd21b4c-df90-35b5-8f1e-5df9288e1d85 | -11.66784 | -46.77784 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87eb76bf-b8cb-3ca4-afd7-3f09b6d3beb0 | -13.17106 | -54.31341 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cd92ba8-8479-3798-83b1-63983994b585 | -10.91987 | -45.39526 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b971226f-bd65-31ba-be5a-2addcdf7eff5 | -10.45932 | -47.85849 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 248612d7-b7e1-3e05-a6c9-d4b835bf72a0 | -6.03639 | -53.48648 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f09a50d8-31c4-3966-813b-8de30faa425f | -9.12115 | -48.816 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55702b2a-d186-3629-84a3-332b35f6fc2a | -13.1706 | -54.30585 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9f1070-5bd2-369b-97b1-f360ccef37f1 | -7.79684 | -44.57278 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7ade4a3-973a-3ab8-a987-abc3673d9fa7 | -11.24066 | -44.87556 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cdd61fb9-1185-3b9d-91e8-5dc9c05376da | -12.19614 | -44.64588 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d8ac19d-1b3d-37a9-a6cc-b37c0769fb29 | -8.9117 | -45.22977 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 84130934-c44f-33cf-a03c-df4d904f5e3d | -13.12644 | -46.32096 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1a79baa-44d6-323a-af00-49c59d0bfa2b | -5.85769 | -53.45316 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23a4bd79-709c-3796-85bd-cd965284dad4 | -6.86326 | -55.78807 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cad966b-3af6-3526-83cf-0241a02e5d66 | -13.12196 | -46.32775 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d265329-c24c-3c15-99ce-cd066f6f37e2 | -11.74874 | -43.63881 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8149045-2656-338d-952f-9edc396264af | -11.14848 | -54.80126 | 2026-10-09 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff0d525f-9690-3f84-8556-7bc26adf18fc | -7.40798 | -44.75821 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8ea275e-66d3-3687-b44b-8835538aa7d4 | -11.63169 | -54.53944 | 2026-10-09 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34ce7250-3a83-3245-a099-8eb7e0ecde98 | -9.86933 | -44.87213 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc3880cf-84cc-3c98-a2e7-1419671eb122 | -7.53599 | -45.87472 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 898b0015-a14c-3b17-9fb1-cf7993220f49 | -6.1766 | -52.8562 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7b16b34-a77a-34ff-ba8d-f6b0d926e605 | -13.37205 | -43.88712 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0cfc75d-55e8-30c7-aa8c-6aab2ba27fa1 | -12.01258 | -43.46493 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1e76282-bcb8-36c1-9a45-48a638076116 | -8.90545 | -45.22501 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0f9ab358-7532-3626-8863-8200e03d2425 | -6.50917 | -55.40631 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f316040-51d6-31b0-85e3-ad015972f309 | -11.08531 | -44.05461 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aaeb4e4-4f6a-3800-a35f-828474b77b41 | -11.19753 | -47.61995 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bec8d6a-2850-3dbb-bfe4-4c74a422db59 | -12.22066 | -57.0944 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 450882e0-3d5a-38f7-b4c4-e31a344297c2 | -11.57604 | -49.77934 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a41449fb-c5d1-3a1e-b327-a75fe59a12f2 | -11.23122 | -44.83837 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33cdf894-5958-3502-8678-b67865ade880 | -7.48971 | -42.79254 | 2026-10-09 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05ec12a3-6477-3427-8c10-8fe84e22ad20 | -7.90562 | -54.71381 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7d78d92c-3245-34b9-833c-345899a86fc8 | -6.93482 | -46.58978 | 2026-10-09 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0262817c-3d7a-3835-8cc6-df790ce777be | -7.34112 | -45.30803 | 2026-10-09 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1d6c850-a555-354a-9964-da7d64533382 | -8.73019 | -45.15299 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6802e21-bcb0-3663-9b98-3723f4770894 | -6.38746 | -55.27141 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5cce0056-db63-3a2c-9ced-806f9c8f673e | -13.75693 | -43.62136 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f69355-d339-3b9e-b9d6-02f1985a1d7f | -11.21967 | -45.26278 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6367cc65-0a00-3625-956a-8c368853c834 | -12.20876 | -57.09926 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8372fde-ec1b-3c3d-8784-83c1bab64171 | -10.93594 | -45.3819 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7aff0e1-bf23-3ca0-a3f9-b0c2c0a2326b | -11.50926 | -48.95852 | 2026-10-09 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 440c7b09-25e3-3349-b32a-a3357c872803 | -13.20655 | -54.36344 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f54e834-f362-307c-ac4c-383b099e48e8 | -13.21088 | -54.36421 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faedcd7b-f840-3c9c-9b04-bdd144c01d34 | -6.23982 | -52.88466 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e633145-2ba2-3dea-988b-76a9a9ce449b | -9.78498 | -44.78018 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6ff9664-3e1c-380c-8748-b9c51f63cef2 | -12.22834 | -57.08821 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 921d1a48-f689-3134-a736-048014e30a04 | -11.83991 | -43.59482 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba0c8327-e920-3702-b0e0-3de5aa12a84d | -8.43845 | -47.03073 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96cc6e95-8119-32ab-a1a6-0fad9000ea60 | -12.20837 | -57.13624 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c29981e-526c-3739-b1cb-660f733e7b2f | -11.74978 | -61.05939 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c06e6a49-8c5d-38c2-9fff-1f3fac89759b | -9.01965 | -44.38004 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6382b176-65fd-3808-baf9-46910b4c037f | -6.24761 | -52.86339 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 072ab15d-1791-3503-9180-8f038d6d7624 | -13.18764 | -54.36891 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4094a04-b0dd-335b-aea2-f965dc871704 | -12.20819 | -57.1301 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4815e555-2177-38d8-9d16-76cf5b232830 | -12.21023 | -57.12637 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39fecb01-136d-3681-b3b6-919a6a4dc296 | -9.0277 | -46.87288 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3295487-8c9a-3bec-ab6a-2133385e0785 | -9.73552 | -46.93913 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ab410f8-2f04-35ee-b6e4-9e6b04fbce72 | -8.98787 | -47.54208 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f89ec93-c426-3ae9-b79f-4b793c334e23 | -5.98756 | -55.36014 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 969c0343-1e08-33fc-a75b-9081f11fd555 | -7.89459 | -55.00431 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7add594b-5265-348e-b93b-9b034c29ae3e | -6.32732 | -55.3322 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6afa10cc-77b9-3054-ae58-d6d5e6e8a335 | -9.87716 | -50.49689 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69313826-44d9-3dd6-83df-4b331b62636f | -10.9861 | -45.39682 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7163eedb-b50d-3b43-844e-c772126fc6e6 | -9.09791 | -59.39145 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0be25ba-acd1-3667-a380-8314d9e81643 | -8.07971 | -45.60814 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6030032-fd4d-396a-8420-a910e7c28da5 | -13.16912 | -54.31417 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fa96de1-1d8b-3eaa-b618-93a6ef4e3662 | -7.61813 | -46.53237 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8d37b64a-bcfb-359a-9389-ade0f125b877 | -13.16319 | -43.28175 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d9311cfb-f701-3bbb-a909-94006584ef9f | -8.98349 | -45.90402 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 39cb94c6-2882-31a6-a629-d3dbf0092ec6 | -11.27626 | -45.19207 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0731a53-ae14-3584-9f7a-91d3d82d357d | -6.1411 | -52.9044 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543b9d27-9746-39a4-b8fd-bf1ffc1dd56c | -9.11716 | -48.81913 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe259f1-6e83-385c-9eaa-72b1278928f9 | -12.16011 | -44.79368 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac282c8a-5ec9-38aa-b200-69386ac5cd37 | -11.84142 | -43.58274 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0dc6f5-5298-340c-a715-83eab72f65c7 | -11.97027 | -57.61196 | 2026-10-09 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a508f8b9-d1dc-37d5-aa04-41d6546cd64d | -10.52902 | -47.32303 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93006886-dcb7-3b6b-bf5a-a91ed7fb24cf | -10.24975 | -49.68198 | 2026-10-09 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c169323-f2ad-3ad8-ae57-e53ccb4b0a7a | -11.18296 | -45.31998 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2334165-8951-3372-8e48-e33de62b0ab7 | -6.24781 | -52.86375 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b64d14dc-7a4c-3277-9423-012d46e3018b | -13.50151 | -44.37457 | 2026-10-09 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f5dd3d86-4b05-3e4a-8d30-d8a1a8830743 | -6.48885 | -55.30192 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd4ad6de-1441-396a-a69b-c01d95d327ed | -11.61108 | -43.71209 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4273813-f3ff-3d4a-beca-7cecd327be85 | -10.0485 | -48.21678 | 2026-10-09 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bfadbdb-1237-3ea1-8200-eb06fd4810f6 | -12.21463 | -57.10297 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18768999-f29d-306d-b2b5-2663c4c7c4fd | -11.61786 | -43.60534 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ade9482-5370-3f87-8b17-9296c01a2cc5 | -12.00689 | -43.44967 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0f6f4b7-af57-362c-ada6-5f10d46d426b | -6.4948 | -55.30577 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808a5a97-0403-3ef0-9e4d-7b40adfd7f4c | -6.21775 | -52.88102 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f321505b-b458-3175-b6bf-c27dd836700a | -12.21085 | -57.12309 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README100.md)
