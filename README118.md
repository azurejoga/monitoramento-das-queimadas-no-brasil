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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250bcf6d-2288-308b-b87a-37349e7ff3d1 | -10.17047 | -43.90112 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c62a395-c239-34a6-aaeb-649971d7d2fc | -6.89607 | -52.47648 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2cbaafa3-4022-3532-b850-ff9f76649aa5 | -6.85943 | -37.73857 | 2026-09-28 16:26:00 | NOAA-20 | SÃO BENTINHO | PARAÍBA | Brasil | 2513927 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3850ad49-825a-3b73-b588-82bb5d3f00b1 | -3.80612 | -44.10344 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a50400f5-5d07-3d70-9fdc-1a1baa70e35f | -5.03701 | -39.90257 | 2026-09-28 16:26:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7c5653aa-20c7-3b3d-a8b7-7dbabd93622d | -9.64198 | -42.33683 | 2026-09-28 16:26:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7e57f26c-121f-3ffe-8705-591b6d9c7740 | -10.12228 | -50.19802 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 90deccb1-e0da-3884-9637-8010913b1b47 | -8.94825 | -45.90145 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 421b3b3c-ba91-3bc4-86e5-b7d95785b744 | -10.11671 | -50.19297 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7019d909-f02a-320c-a887-e657b297fb65 | -7.19823 | -39.26927 | 2026-09-28 16:26:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 457dc143-b6c4-3e1c-92f9-86c4a3ad46b5 | -7.98859 | -45.01121 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66d44477-50d2-31e2-a431-f7115e7e1abe | -6.16997 | -52.91026 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f8c627b2-78c1-3c1e-8902-0c164f57bc7d | -6.20162 | -52.91392 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e4631dfb-c8fd-3a38-b7dc-f039d954fddb | -9.98191 | -45.35754 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8cd0c9dc-2416-35eb-bafe-1f1efad07986 | -10.1171 | -50.19587 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6b40b441-ed9f-3cc0-a14b-dd58e4051079 | -10.88692 | -50.68003 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4683002e-e02a-37a2-8c4e-103722188cca | -6.16209 | -47.12868 | 2026-09-28 16:26:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 70e66380-bd6f-3498-868b-3c4c9713eb81 | -8.35623 | -45.47236 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8bc89a1-8a38-3b4c-9fbe-02de0eb89ecb | -11.13988 | -51.17093 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2401d658-6c6c-3916-b910-736ca5a129ba | -8.73925 | -44.9078 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e80a05fe-5f25-32d4-be60-ab0d77611754 | -9.33138 | -46.42278 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 35dd20cf-8a49-33ba-9878-3d53276e76fd | -9.02612 | -45.01778 | 2026-09-28 16:26:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 88766d15-1742-3dca-b6ce-8425adda8733 | -9.85544 | -44.93916 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 032fe9a1-61fa-35dc-a3e0-1c41869e5ed8 | -10.73328 | -50.47568 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8be37fea-7b20-3ac8-9631-2e95a3a280b7 | -10.11727 | -50.1987 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f601dfeb-c759-3836-b12b-0615b46adfab | -6.15006 | -51.57098 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6898ff36-d9bf-3b28-86d5-5247879e04ce | -9.83348 | -44.93841 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 63b8145b-f35d-367b-84a1-be056731e5cc | -9.35544 | -46.53776 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a556c015-6e86-339f-9f49-176e032c6a82 | -9.02627 | -50.80721 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| cfe3d145-a43e-3138-9bef-f8e8b346c39a | -7.59581 | -55.70177 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3321776c-bd23-3bd1-ad52-b9335051dc01 | -7.50317 | -44.57262 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b7367061-e4fd-306c-8694-3734d033d029 | -11.11823 | -47.72373 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19806aa3-351a-30e1-8c5f-f2518d2c3271 | -3.16665 | -42.27622 | 2026-09-28 16:26:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45407448-1d90-318d-a9ed-bbaabd32710f | -6.21021 | -52.90797 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 33e8f148-03a8-39d5-9766-7001d6f6ce56 | -7.28466 | -41.0657 | 2026-09-28 16:26:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 181ee8cc-7cc9-3e0a-b9d4-6e4a87f3c956 | -7.45362 | -44.5914 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b53a20e-cd0d-357d-b2bf-91b1d1a9ea95 | -9.78816 | -44.81971 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 6d41fc72-fcbe-372b-b19a-611327ea74a0 | -10.1078 | -43.9491 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3621d791-a1ed-3d14-871d-fbb3fdb0e5d6 | -6.91661 | -46.40939 | 2026-09-28 16:26:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 47106786-2cde-3299-b333-dbab99c7c836 | -6.21243 | -52.90805 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c7f9f4b-e9a6-32c0-a8ea-f31d74fb0d64 | -8.03251 | -42.84271 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 95f506f1-53ba-3946-8fe1-f980c670d2a1 | -10.24566 | -44.6149 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5190a2cf-87df-333f-a93f-db57d091a65a | -5.2427 | -43.1508 | 2026-09-28 16:26:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60ad04fa-0fc7-3b49-8654-a0cf2a973e14 | -10.58962 | -49.98921 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a2dbc1cb-a387-3e41-8709-c0d1932fd606 | -6.71912 | -45.58795 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee08572d-63d3-3a8c-9a31-d3524fe25c77 | -6.16379 | -52.8238 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 941fa95a-2d73-37cb-bd03-818cbe34589e | -10.98491 | -50.6936 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e658b346-e112-37ea-a88e-fb2fbdc5cb8e | -10.93666 | -47.58719 | 2026-09-28 16:26:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 27b2342d-30ec-30ba-b97a-056f894399a1 | -9.51735 | -46.3761 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 91d84ac5-d9b7-3c96-a722-a80ea900c9b2 | -10.26097 | -44.62111 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8ad35547-7e97-304d-b4cc-db345bcf19f2 | -8.67317 | -45.34333 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0b6e2993-36bb-3da4-b4ab-b2db503f28f7 | -7.23876 | -44.84378 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be598edf-931b-34b6-8819-6b79802e8fd4 | -7.20754 | -45.07761 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ab8d7ba2-4197-376e-a5ea-a185347140cc | -10.29412 | -48.16488 | 2026-09-28 16:26:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| adf92d2d-31ce-3896-b2be-9b7fb703002e | -7.70602 | -44.92881 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b10e5127-e21e-3d70-b9d8-eeca746952d0 | -5.43282 | -44.65052 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 865bcba7-050f-36a0-b7c8-824dcb3d6ed5 | -10.28614 | -49.97009 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3745efd5-772b-3879-bd6b-8f2396703353 | -7.29207 | -44.32695 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| db94fb48-00c3-3d7d-b94e-d0e8ff9e4579 | -8.5697 | -45.76017 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f432dc78-e5e3-3098-bb0f-0b18b4e47267 | -7.27966 | -44.31356 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3782545d-5ff0-356e-9024-acea05fac89b | -10.97763 | -50.67806 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8721359d-ad14-367d-b787-3854a783714a | -9.78106 | -44.82076 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e1b11b42-f174-3028-ac2e-2d81ce94aa65 | -9.52504 | -46.37499 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f0e25f1c-8454-3700-8eb7-4c84e0caec2d | -10.18802 | -39.69267 | 2026-09-28 16:26:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c9e359fe-fade-36d5-a780-3a89750d00f8 | -10.2077 | -49.98619 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 319aea3a-ba58-393a-9b3a-d3989e20df4b | -6.20872 | -41.5981 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 67d83c35-bf60-3bfc-9f70-df386f6a598c | -9.71986 | -48.02089 | 2026-09-28 16:26:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 41942193-c5c0-32bc-8236-bf8258be51fb | -10.94942 | -50.66527 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 838ec20f-dd86-3c92-9408-9595fb7cc457 | -10.89339 | -50.68904 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 946bef65-9a98-3285-a61d-35db310e175f | -11.14166 | -50.07985 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 02f74c6d-4183-3651-ab6a-915d3fe63204 | -9.82588 | -45.25705 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 156f824d-9a18-3167-8b13-062cc9dfb311 | -12.19251 | -53.40215 | 2026-09-28 16:26:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 807ef3fe-da2f-361d-9df3-771b845353bc | -7.97102 | -45.01371 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e306cf4c-50f7-381e-8756-d23bacb1873b | -9.77162 | -44.83051 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 49ab86d6-377b-33bf-a73d-c93f33f8c27e | -8.96806 | -44.16577 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d9590e9f-91a4-3d9d-8d36-adb3540ceb8c | -10.5471 | -49.77761 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e45f6920-3001-37d1-b677-e3869b1ab485 | -10.22967 | -50.00051 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d46e4692-b211-3128-b73f-d332abb2f3c2 | -10.36194 | -50.44619 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76f4e619-0ba1-3807-afe8-cb5a8cb0c073 | -4.09276 | -42.95603 | 2026-09-28 16:26:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3a5c608c-0c8a-370a-b705-8c09317b54c0 | -7.23407 | -44.86007 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1fbd69a4-358b-3732-8623-a45e9f5bf371 | -11.10969 | -51.33403 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6412e7d0-6474-343c-9ec5-7dd3b9771ed3 | -7.68647 | -54.76345 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 207797b5-1942-3482-b3ef-de7ec2d15f75 | -9.40556 | -46.83718 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5f098caf-e991-37c0-a781-082da38cf11d | -8.96983 | -44.1539 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6509d974-cf5c-3bb0-a220-0c38e0360e62 | -10.1225 | -50.19813 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 8b4f503d-7983-3a2e-967d-190d9875ae82 | -8.73107 | -44.90109 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bc479551-5132-3df2-89b2-1ec17bce5d4b | -10.95145 | -43.88501 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| e348af71-f82e-3853-8307-c39aaac586e9 | -7.34463 | -38.73159 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b37957a1-5de4-3b14-bf9b-2465223ba7f5 | -8.65824 | -45.36681 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c6f7be7-d965-3db5-9fa3-397911bfc5b8 | -8.84142 | -46.58455 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 354daf86-9ea7-3ca8-98fb-df98647c2b28 | -8.10786 | -44.00111 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84e297ce-5d79-37e7-8a97-22d0e496b9ed | -7.65121 | -44.74844 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78449b56-ee11-3acd-9127-f7edc1853160 | -10.10836 | -43.95288 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6c0ee94f-0020-39f2-a875-aceb0e7128ae | -7.15716 | -39.31522 | 2026-09-28 16:26:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8758eb4e-d67e-3fe4-83be-539c1379c471 | -7.50069 | -55.01398 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| f4efae5d-dfad-35db-9a7f-56379ecb37d1 | -7.45623 | -45.80576 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| db8a8009-5ad7-3382-856b-38130e089f9d | -7.27911 | -44.30988 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 1462a9a0-3e49-32af-973d-0ba70f25e0c5 | -9.98665 | -50.13639 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 7d3ad933-2bbc-3c4d-9818-677d3f45015e | -3.88934 | -40.83125 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 66d0e9d3-1f6e-3fac-a854-f0076fdbefc8 | -9.39116 | -46.38696 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |


[Clique aqui para ver as próximas entradas](README119.md)
