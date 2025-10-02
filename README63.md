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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b07857c-089f-34d1-a19c-eaf42a0a4e4a | -9.33983 | -45.69852 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da51aecc-a048-3a5b-89a2-7b22a56485ab | -7.76629 | -42.5413 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 44276593-9e67-3b32-a85e-4d03619445c2 | -11.06144 | -47.80894 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8bd035fa-34f8-3634-9183-e9870827ea5e | -7.79333 | -42.51658 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 40fea7e3-298e-3391-a5eb-5e01507fe78e | -11.27641 | -47.81887 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cb24242-185b-3e2d-a485-35d41ffceb8c | -8.51501 | -47.80429 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82e0329c-3dfb-3168-9801-35f96967cb5b | -7.78951 | -42.516 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 62f9a333-7b91-387d-a093-34fea14bc436 | -11.17293 | -47.19154 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b76271d1-d7b5-3e41-a698-1b35725508fb | -8.74214 | -47.34074 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c268ba5b-c27d-38fc-99c3-88a248d6aa82 | -11.06697 | -47.81711 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4cc5ec1-b6a8-3ab4-b9cf-846920d699a1 | -6.95571 | -45.32079 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52047516-9152-3815-8a31-204f3151951e | -9.39922 | -47.56521 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44a760b0-b83c-3e85-a550-7deeba8df6b8 | -6.71257 | -44.56998 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b304e903-dd1a-3ff1-be8c-033b19dd8b80 | -10.81564 | -46.6206 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4ab507a-e1df-3bc5-b300-7ee53520b4fa | -11.81357 | -45.01796 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8678a30d-98ad-31d5-95be-5e2c41681524 | -9.77475 | -46.21745 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96739e00-98d0-3d85-bb2a-6a70790c572f | -7.72088 | -46.22571 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5367812b-0771-3071-9d13-8fadd0b4c4db | -6.3241 | -43.0507 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62b096c4-2f2f-3091-9e8f-08163e7b91b7 | -9.70898 | -48.95138 | 2025-10-02 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4353e16-c668-3189-93e2-7a03c419643a | -9.40308 | -47.5839 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62d8f5b6-030b-360a-a87e-e65b15bd0b33 | -11.26189 | -47.66049 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bf3ddf9-fa92-3e3c-a175-8cc33b2cadd2 | -9.81436 | -48.26384 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1654730-be18-3885-ba91-a738bc4b18b2 | -6.66218 | -42.80077 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c10774db-8ad6-3530-b880-76628163b0f8 | -10.22112 | -50.33645 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 651ad354-20f8-3a7c-8203-3d4eb5137aa1 | -10.6024 | -49.63789 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71f09137-be75-37c7-8886-1d0eb25a8bd3 | -10.66508 | -48.59492 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7678f39-cfc4-3911-a40f-49643cc1e271 | -10.87072 | -47.81818 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20355f68-4bac-382b-acd8-9b72a31cf1e8 | -6.52308 | -49.76252 | 2025-10-02 04:29:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 376bf265-4718-39b3-8887-751910489c40 | -11.92156 | -47.05755 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a66f1685-6902-3ee2-a857-63e89828f159 | -11.3606 | -44.96577 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08b96539-730a-3253-90ce-438fbf14a67f | -9.9502 | -43.72972 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a257e19-5343-32fd-a31b-d8ba304bc643 | -10.96038 | -46.65072 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07c9ab70-3d24-3e0c-a4d4-d1bb2cd9b818 | -9.77075 | -47.74492 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 554d72ea-b0d5-31af-8c44-de0c6e1a88db | -8.8921 | -46.60104 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbc488ad-1363-31d2-bdd3-7696c702651c | -10.38273 | -45.12454 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd5ce644-ba61-349c-a2ca-b80fb7b4e555 | -6.77276 | -45.58218 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06c27df7-1c38-3a47-aa59-d58901f32dcb | -11.82034 | -47.67883 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76c9881-80ec-3482-b2c3-c2d666b2a9f7 | -10.11457 | -45.35057 | 2025-10-02 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a14b478-c93b-3d0a-9f82-be660ede1cef | -9.16384 | -49.03767 | 2025-10-02 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b97375e4-2f4d-3630-97b4-786a94ae083d | -8.8595 | -47.66273 | 2025-10-02 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc9e64e-434c-3807-bc7a-44579f7e773c | -11.22046 | -48.21003 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc80175-0648-3402-8303-44080800e9be | -12.22432 | -43.76115 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2fbf047-8827-3196-aa68-de3aa3023f0b | -11.00599 | -46.57783 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f3f2f5e-0fb2-3443-ba0c-99c3986ddcd7 | -11.00555 | -49.58326 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0389f3e5-dbaf-36a1-b01f-f1c20492a593 | -11.837 | -44.95654 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 408f7e0e-32b7-3f3d-abc6-8c8437cfab99 | -11.19124 | -47.76112 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fec65d06-8ea5-34e8-bf85-15f6b976230b | -11.17348 | -47.18801 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6cf3141-3106-3f6b-a848-f7d5fe997cf9 | -10.85902 | -46.58388 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4abc1ba-a315-31a8-9d70-dc1731f74432 | -10.70591 | -48.00131 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3f13796-ea9e-355c-a751-cba279829ea3 | -8.55755 | -44.65242 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c6c2339-2ddc-3e80-9a7d-2dacf474215d | -11.86815 | -45.01421 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e002d13-036a-3f5d-b034-c463657f1b69 | -9.81495 | -48.2602 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83c42e68-12b2-3d88-8209-ee2672d4dc36 | -11.10428 | -49.24352 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab178cf9-eae9-3aa0-a975-2a329671eaf2 | -11.84053 | -44.95706 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56c24110-588f-33d8-9b26-ffa2561a1e59 | -8.2082 | -45.52373 | 2025-10-02 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c6e59db-1c3e-3e81-91db-3c9afbbc16b7 | -6.82923 | -41.62521 | 2025-10-02 04:29:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a1d29f9-780b-325e-9d67-17dfcfe4e419 | -9.95251 | -48.78743 | 2025-10-02 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bd5aca8-b1d2-37d1-bd2a-62fa66bee4f6 | -8.90444 | -48.94212 | 2025-10-02 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ee7918-b8f3-389c-8280-d8ce8a8b53d8 | -11.81978 | -47.68236 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e681f2a3-e7bd-31a1-87f0-6bde240456f9 | -11.43792 | -43.88427 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ea6717-e6bd-3807-8c68-1b1cc2e02b6d | -9.33365 | -45.68676 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fdf56fa-aea4-3e91-9776-027f28773e18 | -9.7703 | -46.224 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1accd5ef-8906-39ab-97fd-e2034cf258ab | -11.87169 | -45.01464 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 780b0571-f2f7-3591-947b-caea987be2ef | -11.01682 | -49.81772 | 2025-10-02 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 875a00d8-4268-3f9a-b1e9-d4e2ccd7fd8e | -11.82764 | -44.9957 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9d5861c-5a89-3299-b575-0b0309048f4a | -5.99988 | -44.57939 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3a2dbb2-8771-35d6-aa52-ae4abf9f9296 | -11.81414 | -45.01401 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5997d27-659b-3a8d-ac54-899dd48b5321 | -9.08634 | -46.72176 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bd2c8c6-14b2-3b4c-b4ff-41df3aaac137 | -9.94932 | -43.6855 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24394acd-c345-30c4-80a7-3f17e00702d1 | -10.64476 | -47.45649 | 2025-10-02 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd45bfc9-91f3-3359-adf6-f1918a5702e2 | -7.82653 | -47.26578 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78cc7205-f2eb-3f19-be88-dc5b3763acfd | -9.42119 | -47.36328 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efa0fa86-9a3f-3570-a9f8-fef5facda81b | -10.63974 | -48.51624 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44620b93-7130-3763-8ee1-08c66458f5f9 | -9.83163 | -48.28528 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de14afb8-d6ee-3286-bb6f-500f6a84bc6b | -11.27975 | -47.81942 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5af8839-55ed-3297-8582-d6be617add9c | -10.26806 | -50.3229 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b19c4d25-dda6-3bf6-b72a-afe8acb2a3c7 | -11.12213 | -47.72839 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3a9569f-d6b4-3732-94b3-27146424747b | -11.45434 | -44.96668 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00ea7f60-4a2a-3293-8964-4aaf1b903c88 | -11.43856 | -43.87984 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa0cec28-47fe-3f0f-847a-7381ae964e9a | -11.19406 | -47.74347 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f709e062-f50e-3836-8b3c-b1aaea41f068 | -11.8133 | -45.01902 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 127a2ae4-c851-3756-9260-c07390543e28 | -6.79472 | -45.96585 | 2025-10-02 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30b05c30-5f65-395b-ae59-dffa51f922ab | -10.2204 | -50.34066 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a19a9ae5-2738-3ba8-a054-be5210baceaa | -11.19678 | -47.19175 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8eb8790-c2ba-3ef1-b347-0f356710d489 | -11.35647 | -44.9693 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5b0133e-adf8-3bc0-b1d4-362038457755 | -9.7742 | -46.221 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a02f360-9422-3a2d-9c59-8d5531080d37 | -11.92545 | -47.05454 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a172ad5-4f61-3dfc-822a-44ed7f4346c5 | -9.98025 | -46.17635 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4af1787-af36-3134-a328-19e697470786 | -11.66908 | -47.49901 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 127ee40e-b4ad-3b01-8e0c-3b558cf45c3a | -11.78772 | -47.56135 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eccccb8d-64e5-353c-ade6-b71ad3991555 | -11.26245 | -47.65697 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 243a35c3-2914-3d2d-96f3-fe3f0069e478 | -9.93597 | -43.7496 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 62a7da18-fae6-3c99-936a-e278a5c996ca | -11.4736 | -44.9821 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbd0e432-966b-3840-b963-e0b7113d2b80 | -10.2121 | -48.19551 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bddcb78b-f08e-3e2b-9bf2-94d3f476d4ff | -11.08809 | -47.81333 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08c54ccc-d36c-34c8-8c2a-a337ec53eb55 | -9.91051 | -47.70988 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf39297-7819-36d8-a30b-bd77a507776b | -7.05182 | -43.23151 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cea87257-b5cc-313a-bd0f-279b912b170e | -5.83127 | -45.76804 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 262ced90-e087-37e0-b147-fc45f25e8458 | -11.05159 | -47.8149 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b361c227-482e-3772-9a54-4646cb93f85b | -9.94997 | -43.68115 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README64.md)
