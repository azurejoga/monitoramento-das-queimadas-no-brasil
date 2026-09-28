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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4ccbddc-bef2-366b-9f36-634ecd69f7f0 | -10.1292 | -45.138 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d045b26-5a16-3bfe-a4ce-75cc11971f01 | -11.38491 | -43.42826 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c88bbec-f64a-39bd-8b74-ebb8ff3912bb | -12.68465 | -45.0201 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 032c115d-adba-3d8d-9448-d6e9889e92c1 | -7.88418 | -45.44795 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29246da4-ec58-3202-bebd-494864dcbaa0 | -11.38208 | -43.41817 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49b1db6-b6ad-3e76-9b35-7c435b7472e5 | -8.01261 | -43.73983 | 2026-09-28 03:49:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ae06d736-a66b-3e66-b95c-53752b650df6 | -11.37193 | -43.39705 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea523a14-f3c1-3888-8bdb-10ab73ff488b | -10.45183 | -45.0914 | 2026-09-28 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e195e7c-75f2-31c1-a789-109874f026af | -9.7859 | -44.82507 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b86c787-4d4e-3108-988d-036df7cc7b9b | -6.71847 | -45.59777 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89387b05-a918-35ae-ab65-6e6eabf9b2dd | -8.23043 | -45.44861 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ba1dccd-0bf8-3039-8ed2-0d7a08b2e5ac | -7.07266 | -41.73917 | 2026-09-28 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c42a778b-1fe7-371a-96e8-8272af9174cf | -14.94899 | -39.02365 | 2026-09-28 03:49:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a68c22d-13bb-3ff3-81d3-595851e0b24b | -11.68143 | -44.54915 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7ac12ce-0c6a-342e-9cb0-9b52f0eabc98 | -11.44127 | -44.92861 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89efccd5-1efa-3710-94a0-af848121b36d | -10.94979 | -43.89029 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0afdd092-e5aa-35ce-9d31-c34f9778ea65 | -10.24618 | -44.61535 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63a1bbfe-bccf-39fb-9888-08a2d1654ef3 | -10.21372 | -50.00469 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40ba2f07-db94-3c63-a732-df384c6130fd | -8.23836 | -45.40515 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1863b6c8-1384-3b25-b844-dcec89ab5ff2 | -8.36412 | -45.46481 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a58223d5-7e58-3530-96d2-bc3179e5276e | -6.99807 | -42.62043 | 2026-09-28 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ea76f8c-56d9-35b1-8645-5a84876e9605 | -6.7204 | -45.59895 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bf031c95-1e2e-3efd-ae06-05893319a24a | -13.47081 | -48.60475 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb043a75-6819-35a7-a806-3c299801f5ce | -7.70598 | -44.93915 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b728c83b-86cf-3af5-a593-80e90ef21f17 | -14.91006 | -40.78003 | 2026-09-28 03:49:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cab60e87-ea85-3b71-90d0-415c5c93f931 | -8.89487 | -46.1935 | 2026-09-28 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fe181a6-f920-35de-9229-cebe057bac93 | -12.87793 | -44.78974 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f4800d5a-75ce-3198-96c7-01e9a3625515 | -10.69215 | -47.81822 | 2026-09-28 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68193869-d1a0-345b-88da-a95d1cc3df3b | -2.14404 | -46.18346 | 2026-09-28 03:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48dde245-9a42-36af-ae5e-567f47cf4dc4 | -8.36456 | -45.45899 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dd49522-18b0-309d-aa9b-ed690181fbc1 | -13.45366 | -48.59557 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0c658405-a88c-3921-ab62-d44e74f0e599 | -11.63241 | -46.78159 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b459dda-7803-3ee9-94ce-595d0da12c78 | -8.43772 | -44.87181 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c02ae6a-573c-332d-bd16-38904bb45005 | -11.68059 | -44.5263 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eddf83c-3e01-3327-b1eb-9d7aeb7999be | -11.19145 | -44.80285 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e4120895-0c62-368a-a0dd-46ad11a95207 | -10.89969 | -50.69396 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad3ac805-3493-3046-ab4e-8d0ab538d137 | -7.51528 | -46.61554 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37dbfa6a-95f1-3041-a04d-48580e6972a4 | -9.15028 | -45.635 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5eaa4b6a-2baa-384c-8e5f-32d311e87fca | -13.19883 | -48.32654 | 2026-09-28 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49e51439-fcd9-3e2c-a47d-213a288983d2 | -7.34916 | -42.07299 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 556048ea-563b-3393-99f0-edf65e64bb87 | -11.70118 | -50.60255 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f6effe0-712a-35d3-821e-46729cbd8f3a | -11.60332 | -44.14069 | 2026-09-28 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4390acd2-ae43-3dca-9811-d80fa3e78999 | -10.91788 | -50.68932 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 675abd14-681c-32de-983d-bc57da51e45f | -11.45065 | -44.93386 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3cd729c-446e-32db-ba8d-4469197d7976 | -12.65455 | -47.32605 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86f21882-0442-3688-801b-05173f7c02e5 | -6.72113 | -45.59503 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2b51fb06-5421-3155-9559-53cb1d830aad | -6.70784 | -45.59166 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e903cfd9-ba36-330f-af3c-3a9e8b0e28f3 | -6.69157 | -45.64998 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93dc92cd-361b-300c-8d84-946f098dff78 | -10.91545 | -50.68993 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01592a34-27f2-3fec-af71-76e112344e94 | -8.36965 | -45.46547 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29f0310a-19ee-3fc0-a908-d09583aca247 | -11.43631 | -44.92745 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b8e5a3e-af43-3d79-b183-4f7cc2115dd7 | -12.68229 | -45.02596 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3ac558a8-0d54-35b3-b818-833a3cfd5e3c | -11.1929 | -44.82201 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5cdc5efa-95c1-3aa8-91fc-7b84ec60b2c3 | -6.71281 | -45.59665 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16ab882c-a5a8-39bf-b71a-525f7de846e6 | -9.60297 | -46.85929 | 2026-09-28 03:49:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d34fb4-65f2-35af-9d70-d91c417453a8 | -12.74244 | -47.30215 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 208ae0d1-08d3-363a-9c0c-95f0bc789135 | -13.09116 | -43.33342 | 2026-09-28 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a45effab-ff5d-3ffd-b064-288fa73726ca | -13.37177 | -44.02353 | 2026-09-28 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac6ac0c9-950d-3971-b221-10bc010f1ece | -8.28697 | -45.4202 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d3666f8-8a19-3483-938e-b658111e457c | -11.70943 | -44.52208 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b2f60fd-78e3-3636-a103-0602ea054e83 | -11.83275 | -44.98776 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a54fa00c-319e-330a-95d0-78f8805ea949 | -11.70531 | -44.54386 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b05f43a-9a06-3ed5-9444-ce0fd2255087 | -10.7129 | -44.43033 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b9bd05-2a8b-3911-92c2-9581884107f6 | -10.20288 | -50.01221 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 952e02ae-c2a8-3c2f-92a4-1240e4cd341d | -11.21072 | -44.7827 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e22cdb6-6d6a-3915-abd4-474d2f513394 | -2.14487 | -46.17834 | 2026-09-28 03:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 242bc001-7fb5-3fdc-b97e-d0acc6a630d5 | -11.16906 | -45.13889 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43dfd42f-bd0f-315c-ab73-21df2b69197e | -12.57466 | -43.50689 | 2026-09-28 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9d3ff1d3-f0ab-35e0-8a37-1f50f8d3e18f | -9.77226 | -44.8419 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d1a17d-6418-3b3b-8244-aa14d17c48b5 | -9.97191 | -45.34515 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7926ca37-71d9-3d2f-bcbd-d17341a9b069 | -11.48949 | -47.38462 | 2026-09-28 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eadec1a0-d8f2-3874-962b-d9da2a2f802a | -13.36723 | -44.0226 | 2026-09-28 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a248015-6df4-3783-a3c6-976a63622234 | -9.12645 | -45.61163 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f9687d3-b6d3-3a90-9c89-cc79ec74ed77 | -12.83515 | -43.39671 | 2026-09-28 03:49:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f057b2a3-c72e-350a-82a0-bbdea68eb72d | -7.88487 | -45.44419 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ae2d296-57d4-3eea-95b8-60988a46f7cc | -7.27901 | -44.31452 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 189a61d6-ae0d-331c-8d5b-6a4d3a00a7a7 | -9.79046 | -44.82911 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49b6b0b0-1492-344c-8038-25a0bfa1adfe | -6.9319 | -42.86232 | 2026-09-28 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e01f9b5e-07cb-3c46-a428-0c280978e44f | -12.31279 | -46.41328 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c73d877-fa4b-3574-a904-3891404bef8c | -11.44569 | -44.93265 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42b85447-9091-31e9-a66c-fec82dd5d863 | -12.65402 | -47.32324 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3341c1b2-4690-358f-9e97-187848d9eff4 | -8.66361 | -48.96669 | 2026-09-28 03:49:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22df4c8-3726-3d8e-a709-195048980a95 | -8.36031 | -45.45126 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f73165b4-abb1-389a-8ed8-29bff80790c3 | -6.72343 | -45.60279 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9336cbe5-c25c-3b0a-9789-ac9a244e4e9e | -8.66222 | -45.41684 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c9f754d9-2546-394a-bda7-a07b7a836fc8 | -6.6917 | -45.98069 | 2026-09-28 03:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc310f09-0291-30fd-b8af-552f62a52046 | -9.15438 | -45.64332 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b426e932-dc28-3f24-af0c-54a785f7e990 | -9.62153 | -43.96111 | 2026-09-28 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 285ab10f-2513-3c19-91bb-56d1f5b5efe5 | -12.68526 | -46.98604 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4dde2a-8db5-34f7-a328-bbb89650c5bc | -11.62451 | -46.79213 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3d0b822-4a28-3bd1-a403-0e584f1b4857 | -11.68593 | -44.54005 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 005de9d9-641d-3c9a-b9a8-1454618dec0a | -10.92807 | -50.67642 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89601e6e-ba32-3e6d-95c3-29cb9810dde6 | -11.68343 | -44.5382 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4c80e37-ef25-38c4-8de2-e8b98929d447 | -10.12395 | -45.13736 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 26d0b957-2ad0-324b-a47b-4d17e75c8a35 | -11.18462 | -44.81192 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 55bf1262-1bd5-326b-a523-bfc5f6723a91 | -8.23105 | -45.44522 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d531baad-ef7a-3336-8857-0f867807eb9f | -10.71187 | -44.436 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f557566-8a97-33eb-80ea-6bd7c1adf351 | -12.30995 | -46.40585 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cdf93df-8277-3078-a747-f98504f8d385 | -10.88438 | -43.68449 | 2026-09-28 03:49:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e371777c-8697-32d7-95dd-0eeb7166eabf | -6.67228 | -45.62653 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
