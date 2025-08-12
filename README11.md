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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df6a9231-6efd-30c2-a538-d6f2793995c7 | -13.87837 | -45.5783 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b98a9a-df8b-3c0f-873d-25f3824e4e95 | -17.96228 | -44.29927 | 2025-08-12 03:47:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4593d13-d727-34ee-8fdf-cf821a82cbfc | -11.74245 | -44.973 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3da9fbae-16fb-3fd2-a326-55cd2877dc3e | -17.56637 | -45.33201 | 2025-08-12 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35042d50-2447-3128-a154-5c3bd2148318 | -12.73776 | -45.89753 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fcdf495-f88f-34a4-83b4-de81d983c457 | -14.12321 | -45.37368 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa1a5f20-7300-36ec-8cf0-8e7558da132e | -14.11977 | -45.39154 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67c1e240-1d80-33e7-bd36-1ea4c1f58d08 | -10.96777 | -49.5731 | 2025-08-12 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9db0e39c-cb48-3a33-8b20-a990a243dd1b | -13.02554 | -46.66775 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 866107bb-603e-39bf-b99b-93cb3bc35ec8 | -21.24429 | -46.71944 | 2025-08-12 03:47:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b5f294a6-b762-39cf-bf72-7bb8967a96c9 | -16.00904 | -43.27268 | 2025-08-12 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31053abe-530d-317d-8efe-0eae088dcde6 | -14.63608 | -45.85319 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7127a951-9701-3cc4-9949-f538aaf0617a | -13.02479 | -46.67157 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c66aa0-be76-34cf-a3ce-4e34d9fb957e | -13.03036 | -46.67275 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7d5f4ed-3e07-31e2-82d6-12865c074f28 | -12.57302 | -46.9962 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18e4cb4d-4b3e-36ab-ae97-cea7dbe9b465 | -13.02334 | -46.66827 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6302f666-6fcc-35fc-a0b6-674fa08f31e1 | -11.75374 | -45.03331 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2453cb6a-68bd-3edf-8960-fae050df8c84 | -12.57297 | -47.02635 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 074b46d8-0770-3f27-94aa-b1d3c4988aa4 | -13.34392 | -50.24103 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 040ed306-c9b7-317f-9898-7367d0e70bd5 | -11.45715 | -47.32035 | 2025-08-12 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5614db87-6606-3ad1-968b-d98a8a629d05 | -20.76564 | -49.40335 | 2025-08-12 03:47:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a64e1588-0a07-35ca-8178-19d6d5ae2134 | -15.35635 | -48.40947 | 2025-08-12 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0215f67-f573-3bbf-99f7-8cb4eabded2a | -11.7989 | -44.9354 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f3fc898-f04d-3766-8e11-ec166e42c77f | -14.45459 | -47.84248 | 2025-08-12 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0352ff3-072f-3e79-825c-3d88efe94e66 | -13.62165 | -46.9252 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d78a25d-d545-3683-90ad-e1a348c4f348 | -11.45492 | -50.1659 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f59cc3e4-578a-3da4-a0e5-942c1ba87046 | -10.06593 | -46.39906 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 524235b8-f77d-352e-b115-8ff4f75fe6e5 | -14.11705 | -45.37855 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01f4701d-b967-3aea-a8ec-455ee29804f9 | -11.80966 | -44.93437 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaf06b40-d89c-3baa-a026-8b6017c4df04 | -13.03002 | -47.49014 | 2025-08-12 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ebce37d-69b7-337e-a1ce-a79efbcb3809 | -12.63601 | -45.33406 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff45e238-3e60-33b5-b425-f97c88a461b2 | -13.35751 | -50.24448 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 81d5e296-2925-32ac-8ec2-964fa466c694 | -14.09346 | -44.83381 | 2025-08-12 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea1249f5-c695-3cb5-b543-839b2f396c05 | -13.58248 | -46.94603 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54faa137-39cf-3b9a-8751-e38c2fd17863 | -13.11599 | -44.52295 | 2025-08-12 03:47:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c7541d8-1f45-3bf9-84d4-02469d3202e2 | -11.75994 | -45.02872 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aae0c4fd-b382-302e-8ecd-6dcc18def6e2 | -11.6686 | -50.13285 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 442e1208-7cf9-37f7-962b-4b5d569617b5 | -22.98071 | -49.03707 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 581d4700-0e21-31fe-abca-8ad96b9b68d3 | -15.67078 | -43.48756 | 2025-08-12 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1adeeea-060a-383a-8e57-866d06b2e983 | -11.9116 | -44.85626 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26540a32-ab0f-3cd7-948a-f52bde61af05 | -14.11647 | -45.38153 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 360bf863-12cf-3d22-812b-a46bd36000dc | -11.7681 | -49.10787 | 2025-08-12 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b16c76df-b818-37d7-ad76-55cf8ddab37f | -11.72321 | -50.11666 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a8ebc06-ad30-3bdf-af6c-27fbad7e352d | -12.5681 | -47.02079 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0fe727d-3bfd-31ea-b110-5c95900a9b2f | -11.80399 | -44.93641 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 191d2a08-67a4-38c4-b301-b0897cbf8e87 | -12.5748 | -47.07722 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dfa09c1-8b6b-3fd0-8607-e8fb6a089aac | -12.55882 | -47.00748 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aeec6980-1260-38e3-afaf-79d55299abf1 | -11.80908 | -44.93743 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fab9bdcc-627f-3dac-b5b6-712c041b4014 | -12.98618 | -44.88715 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cca6036b-b55e-3768-a313-b1dc309d7492 | -13.34406 | -50.24051 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d8b7c2ea-d2d0-3174-a49d-fab81aa32fbe | -11.45345 | -50.17278 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c3795c2-9a3b-3b95-85a4-65b61217256f | -10.97594 | -49.56822 | 2025-08-12 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50395151-3601-3924-8009-865d05ae49ad | -13.87564 | -45.56485 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10186285-1f14-39df-9119-142f7b0a114b | -14.02767 | -47.41303 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eacef44c-90f5-35f8-8fa9-23d0f238656c | -13.96322 | -42.58207 | 2025-08-12 03:47:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1054a56c-3486-3c71-b003-5dae8b40ce73 | -14.10972 | -45.38944 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67fe19d9-b945-3386-a735-e45003b255e4 | -12.56137 | -46.99479 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5c5f1ed0-75be-32be-bdd1-07016472407d | -11.75427 | -45.03056 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 770eca5f-327b-349a-8313-77bc74e74813 | -14.1159 | -45.38451 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c3e63f-db96-3423-a00d-b3f582c2eae2 | -11.77022 | -49.11436 | 2025-08-12 03:47:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa456820-1b6a-3c55-92a6-5695d22bd77d | -9.91696 | -46.1804 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c08363f-8243-30f2-91b2-daa884ed6d59 | -15.44934 | -47.01401 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed4f719b-7909-37e5-8adc-fa87ef59fdc7 | -15.4487 | -47.01661 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 873ff869-0aa6-3fda-b57f-0a8293752a64 | -15.35539 | -48.41409 | 2025-08-12 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e72b180-4965-3452-8c01-d68abe20cb4d | -13.34942 | -50.249 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e0838990-ec9a-3681-b75c-f5b80a321817 | -21.2692 | -45.26381 | 2025-08-12 03:47:00 | NPP-375D | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7dc2232-b39f-327d-a25a-2840ca396705 | -22.99219 | -49.03595 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7548f9e5-65a8-3ad2-b46f-1e142e39bc4b | -11.67772 | -50.13545 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e3d9fc3-7d32-3900-b9ee-33fe8833c625 | -17.65582 | -46.68944 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 238b3860-cfc4-31f0-8c3c-3ae897bea0e2 | -19.43498 | -44.31042 | 2025-08-12 03:49:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23659092-7dae-3e86-8da6-8a832d555bd5 | -17.66158 | -46.68739 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d910f925-70cd-3a73-a319-086fee369060 | -19.71558 | -46.22443 | 2025-08-12 03:49:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0a3df0c-cb1a-360e-bc58-6bd5ad5133a2 | -17.66415 | -46.67469 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2ade204-86ce-3c64-b025-7d312b26a020 | -17.64305 | -46.67341 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c851bc1c-9d37-39a0-ade7-a1f438cf1d45 | -19.29907 | -48.42874 | 2025-08-12 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8db10e2f-0bae-3ecc-bff9-e29c62b34f80 | -17.65456 | -46.66933 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb3c81cf-e775-37f3-8a1f-914309f3e94d | -17.66223 | -46.68422 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 83426821-9252-3bd6-9cfd-421426668f58 | -17.65711 | -46.6831 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 092d9363-6cb7-34d5-b789-65bfd05ce047 | -17.64751 | -46.67773 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2323b5c9-0ea0-368f-91da-ce763e2c1eb3 | -17.64558 | -46.68723 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2be69ed1-2a79-3c9c-b267-2f6294ef3dbd | -17.64176 | -46.67974 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f6c350bc-3d5e-32e8-b36c-95014a7134e3 | -17.65392 | -46.67249 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78cd3762-7e91-3966-8716-3c5dd443b0b1 | -17.65904 | -46.67358 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7635b257-9a12-3b68-bc1e-11686305f9e4 | -17.65968 | -46.67041 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01e68f9e-06e1-309e-abb7-a9795c9535db | -17.6507 | -46.68832 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d58d6474-4415-3f41-8a8c-d35e0a062166 | -17.66734 | -46.68533 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35887fc2-89c7-308e-af8a-f10c120473c7 | -17.64687 | -46.68089 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0084f1c3-fae7-3213-ba22-339298ab7f0c | -19.71709 | -46.22378 | 2025-08-12 03:49:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b3b8b47-6d51-3543-bcc4-0e28b8a7af50 | -18.62243 | -46.86103 | 2025-08-12 03:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e839c606-7edf-37e6-a00e-23cb07b593f3 | -17.6488 | -46.67139 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa076c22-8fe4-3b06-9cfa-7b42003d5cf9 | -17.64434 | -46.66709 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ab23f033-4a42-3960-b7a8-35648ddce49c | -17.65006 | -46.69151 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1f0f36e-53ba-3434-862f-78cc876b5d28 | -17.64111 | -46.68292 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| dcfec1b5-d712-3b96-9071-6943481da34f | -17.65264 | -46.67881 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| daffa3d8-c14f-3b71-82ce-d724478600bf | -17.6584 | -46.67675 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 457254cf-e2a6-3d3d-873b-842212f2cf02 | -17.65135 | -46.68515 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 38428d7f-bd61-3990-9391-fe089ecbe034 | -17.6603 | -46.69374 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bd18ca15-e30c-333c-b5ac-bf856659e897 | -18.60756 | -43.90717 | 2025-08-12 03:49:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12ac17ab-93f5-3d3c-82dc-90931d689911 | -17.64816 | -46.67456 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4f844c97-d5be-3524-897f-550caaa8acc1 | -17.64494 | -46.6904 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README12.md)
