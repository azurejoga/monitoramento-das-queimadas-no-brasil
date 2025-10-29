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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97c20428-1f30-33f6-98ed-b038b783ff72 | -10.68016 | -44.58532 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cab35b27-f2bc-3229-b67a-c3050e6a7228 | -6.91829 | -46.02831 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b97076-5df1-33d1-b9e2-6d306e3ced65 | -7.14972 | -45.80711 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb8f832-3f0e-3944-b8fc-ec6082c19651 | -6.2978 | -41.8782 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 7c8e6f5e-ac8c-3739-a73e-786fc76f35c2 | -7.96614 | -46.74185 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8ba9eed-cbc2-3d61-8f73-1f5c9b057292 | -7.89035 | -45.68766 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96c3bddf-dfde-3f49-b618-a9d43e639dce | -7.43527 | -45.12114 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8673cdd9-8e2e-3cd7-9e1c-ddf9df922865 | -9.1941 | -48.30571 | 2025-10-29 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1677654-4942-3ef5-8b90-24c2385cc139 | -10.9103 | -47.80685 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b661fb81-b72b-35c9-9b96-83db45e2b169 | -7.80149 | -46.44236 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 278dd988-6247-37a3-8983-8b5512e8e02e | -8.54409 | -45.6843 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e11f9c67-6fc5-3f2c-b173-2cf00e974d21 | -8.20765 | -47.2976 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97804a62-c6ee-36e3-935d-773fc18a26d9 | -7.12581 | -47.20127 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e9628e-89b8-39fe-859f-6c0843e5d5e6 | -9.5005 | -46.93573 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| babd2325-a7d6-3b4b-81a8-b793e02b226d | -10.65245 | -48.01676 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbe87c27-cb28-3059-9abf-3defb398bcc0 | -5.63479 | -47.61204 | 2025-10-29 04:23:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 132b6e12-8600-371d-9aab-21d229987a43 | -7.85527 | -44.23276 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55235e3b-bc30-39d1-a6d1-ab12e80f5db2 | -10.91184 | -48.00359 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56076588-4b2d-378a-b716-7624f1b12981 | -8.05542 | -46.94591 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 684277fb-8788-34c8-9cb8-2863c0c21020 | -9.2865 | -45.22295 | 2025-10-29 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bf8c378-49bc-3638-8b4a-128392bc4741 | -7.79619 | -46.47506 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 186a3182-7280-367b-a644-36876cfed896 | -6.11715 | -48.10435 | 2025-10-29 04:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2ac60f1-2808-31af-a63c-8aa2a2308b5d | -10.65439 | -48.00489 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| baa0c893-b0d8-3eeb-b663-3b0ab6798db6 | -8.61488 | -44.80481 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cb8a569-648e-3f07-8887-1453cb58ada4 | -10.21716 | -45.95054 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 841a5f92-056b-33dc-851a-279df6b1d328 | -6.14941 | -43.24264 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 720f1060-a60f-34ab-867d-e34071f2ec0b | -8.23968 | -46.91001 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fd575fa-1b34-36e5-874f-70f76d3b1394 | -7.985 | -45.53439 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 689bc37b-f698-34c8-805d-8825931bea46 | -7.85916 | -44.22976 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f11c953c-9a78-3a3d-adbe-989f2f171d21 | -10.62472 | -47.88146 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec2bd91b-73e9-3a97-b6c9-b1f88090ad9e | -10.77563 | -45.11124 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 715b1698-deb7-39c7-a5bd-9dced061328e | -7.92326 | -45.70744 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcdcdf3e-a4c9-32b3-a186-50a99db9ccd3 | -10.08534 | -45.32894 | 2025-10-29 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69707363-0c19-32da-80de-7d59abb414eb | -8.24933 | -46.9148 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c900a7d-dad1-3dae-82da-b8f4b1ee5b0a | -7.16165 | -44.84246 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce46e476-95bc-3ea5-a650-e91e82354bb1 | -10.85042 | -47.89087 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 877421e1-c45e-38ff-bb42-8138d6dc96e5 | -9.80638 | -47.60868 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7dbf056-7af0-3d92-ae9b-58b8aa36538f | -6.60437 | -44.64027 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef76520b-aed2-3886-8973-72ad85eef59f | -7.96153 | -46.74865 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74d8abe8-d383-3788-ae2c-129072098cf6 | -10.76272 | -47.89682 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acd917f7-1970-3afd-96ef-b04a8459d370 | -6.17612 | -41.67799 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2636527b-e69f-30e0-96f4-45068e9ba23a | -10.92226 | -47.6035 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dbf5015-1b4f-3ce9-9454-c790e54745be | -8.54298 | -45.69131 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8ef371b-44eb-3eda-9a2b-6588bf76db6b | -10.51786 | -47.72321 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e06caf-4e80-3611-85a9-232e1299150b | -7.79178 | -46.45944 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daa47390-7664-35e7-b4ac-8245e7657885 | -7.28063 | -46.89455 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 58295b74-a45e-38f6-b110-a1f0b7d9b418 | -7.43472 | -45.12462 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd19b0b2-f638-3b2a-b86f-f52b5034efcf | -7.27234 | -46.88961 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5259c81-a0c4-38f3-9a8d-a23a7b660955 | -7.92222 | -45.6498 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 197a339c-b066-35b0-b4fd-7535566680e8 | -8.24309 | -46.91058 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d3e0ad3-c172-319b-ac29-f2eed330a4d7 | -10.96749 | -47.83915 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3da62ea4-888d-327e-8d74-ba2bc4126568 | -10.60614 | -48.03708 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5754cb2-e435-35f2-a9f3-4660f0ca58d2 | -8.03675 | -47.40949 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28286441-00f4-3617-a9cd-9b42f054ec27 | -7.64083 | -46.91805 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18d146c2-de5a-3191-8824-abb304373a7b | -6.71928 | -43.57603 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce5c05c4-cc8b-3aac-b10a-3202d78dfc6f | -6.85192 | -43.79721 | 2025-10-29 04:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c085a52-b046-3c9c-8b25-0e3ea3719c9c | -8.66755 | -43.92344 | 2025-10-29 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04296d26-c8d4-3cf3-b701-06b48c343e40 | -7.78384 | -46.46558 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1158c860-a3d0-3780-b105-25b06e53cd99 | -7.64567 | -45.24043 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ab9169f-664f-3f2a-9ff0-7b6ac635eb5d | -10.76745 | -47.88969 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 837f3256-43e6-369d-9e1c-083ca7b95c4a | -7.18457 | -46.73843 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6044716-1511-3a7b-ab94-a3b70dcd2357 | -7.30479 | -46.31831 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 95fa8a3d-d43b-371a-a822-52b97615de66 | -6.13519 | -41.70567 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| de78899c-dd01-3f83-ad4c-884636aeb448 | -6.60133 | -46.28017 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cba4ad0b-d5fb-3ce4-bc11-9433d7706ba4 | -10.60733 | -49.62065 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2659eaab-221b-3c17-90a3-17b7414cb7ff | -10.66776 | -44.79956 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ac379dc-8e37-38b1-92c4-aa31732c4ecc | -5.64479 | -43.27925 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e79a0d-8322-3bd0-8bcc-f19022d80cf2 | -11.00117 | -47.76336 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d128277d-d010-3e3f-8b57-f4ce205f279f | -5.1641 | -46.16203 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b25dcc6d-dffa-390f-a8f8-720f0a051382 | -10.75029 | -44.75434 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf737f9d-f47f-370c-9bd2-1f5f6e23bce7 | -7.79634 | -46.45272 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b21c7b80-94dc-3fa2-a375-16fe05f45893 | -9.8852 | -47.45082 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86f31c27-4131-343b-8ab2-c9bec2dffb98 | -9.48805 | -47.01256 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5bd1f7e-b8da-3417-af7b-abd95c011bc4 | -8.03265 | -47.41277 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23495bc3-ed9f-328e-88d2-e45415898628 | -6.16171 | -41.82151 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 16430739-1be2-3530-ab21-d4adb9d4070d | -6.54284 | -43.5635 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e75b67c3-1669-3570-bfa5-d051b8d64724 | -6.10708 | -42.43609 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| df2e48b9-4f91-3331-a591-e98f77ded0c2 | -6.97352 | -49.40269 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b337b6f0-7eb0-325d-9362-042c1f4b58c8 | -8.25987 | -46.35319 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5226a413-2273-3874-8479-772670315c8d | -5.64425 | -42.81159 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0120c7a-4920-3fc5-87e2-44ce8810f765 | -10.65503 | -48.00097 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 642ee2cf-57ef-34a0-b09b-dde673b4f95d | -10.64332 | -48.00695 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d673cd55-4a7e-349e-9e8e-9c8cfae0d977 | -7.86195 | -44.23381 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b02f09-33dd-3ac6-a6d0-72e513b366e7 | -10.12527 | -44.83378 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4206d52f-aebc-3be4-8968-aae4fd27991e | -9.26932 | -46.2705 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bab3536-20ca-324c-b1d8-49c6fda106d1 | -5.60707 | -49.12087 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 827a5e35-54fe-36e1-87d5-a79066546e11 | -7.34911 | -47.64315 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aca9033-709b-3297-a857-af479314c4c5 | -5.68698 | -42.82908 | 2025-10-29 04:23:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4149708e-4229-325b-a572-856adb96c96a | -6.6508 | -44.60495 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e04e2e0d-c433-3654-b9fd-a9867d929e4f | -5.60987 | -47.1091 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a10fe910-ff5f-3a46-8f55-4ad0ac4afcba | -9.50992 | -46.51419 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8387319-9cf2-319e-a693-f46f505f829b | -10.5125 | -47.73415 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20d2e79d-5a4c-379e-8bcc-7df3bb652b68 | -11.26184 | -45.52499 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 100202cb-0e2a-312c-9a42-202139b5384c | -6.8013 | -46.40568 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7030b6d7-4bbb-3cea-9c72-4d95814dbebd | -7.87235 | -48.41886 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93d0014a-fee5-31ca-8a70-87dd8102c28a | -6.99841 | -49.00943 | 2025-10-29 04:23:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dabc01ef-50e2-3b50-b0f2-1ca2f2033c47 | -6.14606 | -41.67532 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 914ce23e-55c1-33fd-9e6a-96ae1fca03aa | -6.20752 | -41.83265 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1ee5b6e-4e7e-3619-a2fc-2c2793512959 | -5.07141 | -47.11177 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa0a7d2d-0768-36f1-bb3f-d217a31236e0 | -10.86944 | -46.04155 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README33.md)
