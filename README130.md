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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc47fb3-ea51-3a92-aff5-b3235219fb15 | -8.4824 | -46.2912 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 3feae962-529d-3f59-8ecc-7c3a575f5fe8 | -3.9134 | -41.5687 | 2025-10-07 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 9ca523db-5a6d-36f1-8dda-88760f5bdb34 | -8.6835 | -49.9419 | 2025-10-07 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| be43fd7e-c06a-3593-9b9f-63aec1e662db | -8.8986 | -47.6483 | 2025-10-07 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 9a0a50f1-ffaa-3492-ac77-5e773117edff | -3.0253 | -43.3339 | 2025-10-07 14:40:00 | GOES-19 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b6615e89-b8a1-38c5-bfd5-fe30cdd3cbda | -8.5584 | -46.2387 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 3c7f42bd-b0cb-3c7f-b26f-17151b655cad | -3.2713 | -42.6457 | 2025-10-07 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ef563cfa-9e3e-3e48-92b6-a60cfdd76806 | -9.467 | -46.0286 | 2025-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0da27fd6-8dc8-3087-b0d7-b58ba504e3cc | -11.8823 | -44.9583 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 8341613c-b978-3694-9069-db8e72f85024 | -4.2847 | -42.0248 | 2025-10-07 14:40:00 | GOES-19 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 3f7ecd09-7573-3321-8039-2844def47c3e | -13.7927 | -45.7627 | 2025-10-07 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 01454a6a-37a5-3b38-ba2f-70764647cbcd | -10.0409 | -48.2755 | 2025-10-07 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a8960638-844d-357e-9c89-c54bec4c2275 | -4.0382 | -42.5129 | 2025-10-07 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| d7685d4d-e045-3012-9144-006301e43f55 | -11.2921 | -48.2841 | 2025-10-07 14:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c6baddf6-97ce-3727-9529-b6f30c58665c | -9.4068 | -46.2831 | 2025-10-07 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 7ac497de-d0da-3a7b-a647-a8de73de1701 | -7.4666 | -43.0909 | 2025-10-07 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 166.1 |
| 80bf484d-adce-3656-a503-1630de8a9e55 | -9.7463 | -47.7144 | 2025-10-07 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ae48e317-1a00-3f2a-b049-9843d8509fbf | -10.3151 | -50.3634 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9e9754c4-2126-3a64-a51a-1cf0af809737 | -10.2136 | -45.5087 | 2025-10-07 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 930688a5-513c-314b-bae5-a1f48252c879 | -3.4179 | -43.154 | 2025-10-07 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 89b6b2ae-5db4-3b05-87b8-79896f0b0283 | -12.0511 | -45.164 | 2025-10-07 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a4ad9c52-7d98-312e-87d6-e2158c4715b3 | -10.3343 | -50.3402 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c2ee8453-a062-3621-819e-2b9eb53d30a7 | -10.2406 | -50.2857 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bea646c7-5f6a-3a42-86ba-21335f0642c5 | -11.487 | -43.4981 | 2025-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| a076f2c9-03fb-3deb-9e9c-c034caa72596 | -12.4919 | -54.7158 | 2025-10-07 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 39763799-5c15-3010-a808-9b86548e525b | -10.0406 | -48.2974 | 2025-10-07 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0e75320a-5198-3ce4-a986-19876bad9bfc | -7.4669 | -43.0674 | 2025-10-07 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| df8c8c0b-cbb3-342f-a6bd-94089fd8ccbd | -10.8921 | -51.0269 | 2025-10-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| cf951dc3-0d2f-3aa0-85b0-568004222fe1 | -8.501 | -46.3117 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 73253d57-b100-342f-8167-b48c8d92088d | -15.6202 | -52.5501 | 2025-10-07 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| cd80d925-330d-39d8-ba88-19cc64b450cc | -8.5395 | -46.2406 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.6 |
| cd3dee2a-fe48-3ad8-9892-86b918ef6e40 | -9.6614 | -45.6667 | 2025-10-07 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 20a59674-5a50-38ea-89e1-5007f8a59520 | -15.5808 | -52.5769 | 2025-10-07 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 15cb87c6-74c8-3368-b27e-513c038dda9c | -8.5602 | -44.6264 | 2025-10-07 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4abce911-e7d6-3c91-b520-41c085ee78e4 | -8.0866 | -44.791 | 2025-10-07 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 04e3491a-13b7-3afa-9292-8eb52a2aaa30 | -3.4917 | -43.3136 | 2025-10-07 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ae3b3919-8d88-3443-b08d-004271030fab | -7.712 | -46.2531 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 60f42575-7cba-3c3c-be09-b8125dacb99b | -10.2129 | -54.1262 | 2025-10-07 14:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f088100a-f0e5-301d-843e-fa4e645c8964 | -10.3854 | -47.9956 | 2025-10-07 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6ef031c9-e7d8-3905-86ce-a5a0313ed5a0 | -11.8447 | -44.9176 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ae5c0f57-c07d-3307-9ce5-6070d2452d56 | -14.8641 | -51.4373 | 2025-10-07 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| ca757777-7993-3473-8399-18508da0ad0a | -11.2925 | -48.2621 | 2025-10-07 14:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3daa531d-8fd1-3e4c-922e-936ae4657df9 | -11.8635 | -44.938 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 95ba5e17-a0eb-340a-bc7f-b5ac9f2059f3 | -8.1055 | -44.7891 | 2025-10-07 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 34eb5af0-f278-3f1b-a735-fcc50cc64dee | -11.7409 | -45.371 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 0a5809b8-4c51-3b5e-92b9-027c2636048e | -4.4446 | -43.2164 | 2025-10-07 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 03a19709-dfdf-3efe-b489-75ee0f185c88 | -15.6007 | -52.5529 | 2025-10-07 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6e7cc17a-120c-35ce-8bad-0ac0ff7ae783 | -14.8835 | -51.4346 | 2025-10-07 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bd11f222-2f4b-3609-b154-0c058e845e3e | -11.0448 | -50.926 | 2025-10-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 20472065-7bed-31ad-91fb-b61d7baa061f | -8.8988 | -47.6263 | 2025-10-07 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 84a546db-1390-3ea7-b283-7271dd134ff4 | -15.6003 | -52.5742 | 2025-10-07 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a114dd82-fee2-3097-85b5-3ae85cef5a2c | -3.1953 | -42.907 | 2025-10-07 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b673c769-bd86-3a33-af18-846dede8b80c | -8.4819 | -46.3361 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b705aa1a-ba77-346b-9032-65eeb26d1114 | -15.3737 | -47.3201 | 2025-10-07 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7da869c8-d57b-32d0-a5a4-15ff679e7d03 | -9.6588 | -55.0834 | 2025-10-07 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c732011b-e872-3b6d-b6f4-f5f104e7c8b8 | -8.921 | -47.3595 | 2025-10-07 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6ad43481-c5cc-3b68-8bd2-43961062c964 | -3.1964 | -42.696 | 2025-10-07 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2c36c203-2d1b-35ee-8287-6345598eb903 | -10.334 | -50.3615 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 73ac41af-79fb-3132-8e16-4fcf80dba5d1 | -11.7198 | -51.4677 | 2025-10-07 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2d3214a4-4314-3c39-b4ab-c314fbb29445 | -12.9294 | -54.7333 | 2025-10-07 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| c12055d4-48d3-344e-8380-4111f318f142 | -11.7217 | -45.3738 | 2025-10-07 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| c82b98fc-e7a3-3366-8b5d-8345847903f6 | -9.0326 | -50.5912 | 2025-10-07 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3aad139e-697d-32ac-a2aa-50bda840fad6 | -4.7437 | -43.2212 | 2025-10-07 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 45db9fa8-d045-3a14-84ec-0250f5b872ec | -14.9414 | -51.448 | 2025-10-07 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 1043525e-209f-3247-a528-42c6fdb0981f | -3.4366 | -43.1532 | 2025-10-07 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2f6f57ad-895f-3bb1-9bb6-3a861591b77a | -5.3063 | -43.0897 | 2025-10-07 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 005ebba4-aee5-3f99-af0d-35e8d06b057a | -8.5207 | -46.2425 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 6867ca0a-ebfe-37e7-ad5c-f80cb29b0f74 | -12.7637 | -50.4921 | 2025-10-07 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 6df83cd2-36c5-34cd-9ccc-44d28c583df8 | -11.7201 | -51.4465 | 2025-10-07 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b7002700-8da3-3e43-939d-292cdc323325 | -13.1784 | -50.8905 | 2025-10-07 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 77bd6250-f88c-3682-899b-6a3093cc3a11 | -7.7308 | -46.2513 | 2025-10-07 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 07128df5-5db1-3030-9dba-682762bd8900 | -13.0779 | -47.8234 | 2025-10-07 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 405a6425-c13f-3301-afec-43848986aec8 | -9.6287 | -46.6394 | 2025-10-07 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| ab24d0e4-611e-3c7c-877f-7cc64d958693 | -10.297 | -50.3013 | 2025-10-07 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d6cab17e-696d-3960-8a6d-fd54541ac173 | -15.6198 | -52.5715 | 2025-10-07 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 68121ace-dbc6-3d6b-baa7-efbb9c119faf | -11.0451 | -50.9047 | 2025-10-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1b7b4bf8-d3ef-3f7f-9f7d-e06d95e66788 | -11.7389 | -51.4656 | 2025-10-07 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 29212e50-ad2e-31eb-81c1-acf4edc9f5d1 | -13.0775 | -47.8457 | 2025-10-07 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |


