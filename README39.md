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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32302be0-cfbe-3a18-86b3-e9233f1b1c27 | -11.73072 | -43.66074 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fb6acaba-56f3-3d8b-b3ee-87abf2edd418 | -9.163 | -45.11503 | 2026-10-07 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02f5afe6-2a0c-3c23-bc5b-8802ec0ec061 | -11.78774 | -43.53765 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ac314fe-a7a6-3276-9db7-434f155b4d59 | -11.73702 | -43.64977 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f395d780-cec3-396d-9862-2b5bbb27ca52 | -11.22556 | -45.26646 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f05c6bd0-94e4-3d7a-af13-ca0e2bb8c38a | -7.81811 | -46.86622 | 2026-10-07 04:02:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6624615f-497a-3582-bd24-addb984e57e2 | -11.07639 | -45.64191 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20fe5085-6212-31e7-906d-de8e6414b581 | -7.87649 | -44.18799 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6cfed48-d2c9-34f0-a08e-4eafd28c9877 | -11.33362 | -46.66772 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f9fd783-133a-3aef-8558-d64914966342 | -11.37307 | -46.68621 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6acb63d4-d68d-358e-8ed3-34dc963baa65 | -14.24833 | -41.6238 | 2026-10-07 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e9b9fada-d22e-3168-9808-84313b677ef9 | -13.86182 | -43.75645 | 2026-10-07 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1930d0fc-d598-3c40-8718-147fb1efae7e | -13.63701 | -44.42306 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c85aa659-32f6-3733-bd47-85d20f564a4b | -9.82963 | -44.78847 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 390199bf-4305-31fe-a72d-3694b3a119f9 | -8.21178 | -46.3447 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c9fd661-f7e4-32ed-a539-a21b154f31a3 | -8.6024 | -45.65248 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1e77069-8b6e-31ba-b53a-8041b20d178d | -8.1998 | -46.34967 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f900854-fc10-3dc7-8075-3d85321a9b67 | -9.80144 | -44.78347 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ceab0e96-4e23-378e-9fa1-d21e2cac5d97 | -8.44492 | -46.41101 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4169ffd-28d3-3332-aa0d-62cae5ab1385 | -11.72861 | -43.64817 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0bb4ea9-e425-3133-b5cd-191d85925bee | -7.4093 | -44.45458 | 2026-10-07 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d47f1f7-dc85-39a7-9382-752c698f41e6 | -10.4736 | -46.82464 | 2026-10-07 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68758e38-58b9-3450-b56f-7300e01b2647 | -12.82693 | -45.5568 | 2026-10-07 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ed25d53-3714-3e38-9182-69272665fa5b | -8.58806 | -45.67316 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b172aaf3-dd74-3365-81f4-11efdace6c53 | -12.17188 | -44.71476 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dde2c70d-a45c-3ceb-b2bb-db10873f296c | -8.706 | -45.20001 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f89aef61-8dcb-3b56-a717-59c40f7f1e0a | -8.1875 | -45.14213 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd2e9a11-be93-32f6-b977-147e5eb2412f | -11.00598 | -45.44366 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dbed965c-fa6b-3e43-8bcb-96af27652ab6 | -8.78415 | -47.57948 | 2026-10-07 04:02:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f4f88d-022d-3aa8-95e9-eeb1544612f3 | -13.5075 | -44.3685 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 04383f60-ed49-3e45-9c0a-addd01c42d55 | -13.75678 | -43.62254 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b30fdf49-65e4-3d1b-a2c5-2db476481b47 | -8.70499 | -45.20559 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d9e5bbf2-2f46-3068-9957-6d27f37237e1 | -8.28829 | -50.27336 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 92d77919-083e-3f1b-b296-ba760c9b89a4 | -11.68035 | -43.62637 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d878bdc-6a0c-368b-9213-a29f4c9a6d0c | -12.16586 | -44.25359 | 2026-10-07 04:02:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15ae4bb4-e2b5-353d-9b33-fd1f21c58105 | -11.37952 | -46.68049 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5861ccb3-480d-3368-b0e3-1aef083db129 | -12.17105 | -44.7193 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3090a52c-87b1-3199-9ca8-7eac7bf37ffe | -11.58488 | -48.59752 | 2026-10-07 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbdcc27d-8ff5-349c-8d26-325f7e9096f9 | -11.0108 | -45.44447 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef28822d-8006-30da-a71b-7594f4c1aacf | -10.48704 | -50.43864 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 651d5228-57bb-3715-830d-1c1d51ce9f87 | -9.92892 | -46.80112 | 2026-10-07 04:02:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd5c91c3-459d-3047-a214-af8098296f5e | -9.80041 | -48.92069 | 2026-10-07 04:02:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46cc86bb-c847-300d-87e3-06b3dd91d8e4 | -9.81553 | -44.786 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fef49e0-aefe-3c90-8215-067bf864541b | -9.62961 | -48.88577 | 2026-10-07 04:02:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7394ed37-55db-3b21-8b3f-071da99288f4 | -12.20489 | -44.66047 | 2026-10-07 04:02:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1cf5e73-cabc-3746-95cf-6041689c7492 | -7.47584 | -42.79553 | 2026-10-07 04:02:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6502a83f-9078-3c4a-b2bd-b4772e74f2f6 | -11.66843 | -43.62022 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4428e80-e699-3534-bfab-548dffe682bd | -8.2064 | -46.34382 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09e9f640-9a75-355a-8dc5-6f6c06a5f013 | -11.75079 | -44.93822 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1692eec1-c1b7-3fa0-9357-1105c38401af | -8.28952 | -50.26713 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c3f0647a-a7ea-3a41-a0f7-72e771394036 | -12.16009 | -44.70323 | 2026-10-07 04:02:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62026ad7-bccd-3465-946e-e9303922b3af | -11.22938 | -45.27237 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a68233c-61d8-3f69-9b52-7aba44037f3d | -11.20994 | -40.88298 | 2026-10-07 04:02:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 562501e6-a9a6-39f5-ac62-f6758db1f42c | -9.53899 | -43.03535 | 2026-10-07 04:02:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b1b686de-cc4e-3c7f-981e-20d78e608d99 | -11.69988 | -40.11225 | 2026-10-07 04:02:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 682eaea9-0cad-3a00-b7df-5d74afa62a3a | -11.10987 | -45.73246 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d30daee6-c827-3adb-9e2b-a053cb9db17b | -11.74616 | -44.93763 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30b9674a-2332-3516-93c1-3e2176ae56ce | -13.26808 | -43.99865 | 2026-10-07 04:02:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d6575f-aba6-3331-b6aa-588188a74966 | -7.27387 | -46.15278 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 811db8df-6645-32c6-bd9a-461f2c68a549 | -11.80102 | -46.70345 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f06da63-852d-3203-9e9e-42cc990144f4 | -8.71394 | -45.18428 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae413be6-b018-3190-aa3a-3e3e2d3b21d5 | -11.73563 | -43.65761 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1bbd1ecb-e732-3a7e-a8e8-e08d75c5651e | -8.19865 | -46.35598 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d22a4d7-3acc-342a-88cd-8bae53f99b6d | -10.06327 | -36.4299 | 2026-10-07 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1070560-c65c-3fac-896e-5fc121fbcb42 | -8.20999 | -46.35455 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c06ab43-d1c1-369f-a098-9d4e9004c0f7 | -11.45383 | -43.39141 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9df725d8-d25b-33cc-b0a8-f20a358ad05d | -13.39471 | -43.87275 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e806effb-cafc-3bbc-b79f-b577e96cc74e | -14.24907 | -41.61953 | 2026-10-07 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 03e195d9-aebc-3b41-8b2d-62b2965aab85 | -8.71477 | -45.20772 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d2bb8c5e-2681-3f12-86da-53ccc64b007c | -11.32603 | -46.67924 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1b4ef8b-883f-3f9c-b657-2322d7806348 | -13.39401 | -43.8766 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1213b06c-11bf-3fc7-9c15-ae1607e94dd1 | -8.92848 | -44.94403 | 2026-10-07 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 533c5d40-abc9-37a6-8de0-4c4b2f90d302 | -9.79951 | -48.9254 | 2026-10-07 04:02:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4326431-b259-3f4c-ac97-1ca27ac14e12 | -10.99864 | -45.43533 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee1d9462-5b1b-3494-acb5-37f5d1da8a71 | -12.21239 | -44.7065 | 2026-10-07 04:02:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23a57901-00b3-37a7-b422-ef6ef8d74d24 | -13.50326 | -44.36747 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cfbd2fb7-d5da-3c15-a9d9-28944d733e81 | -7.02288 | -45.29548 | 2026-10-07 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65634715-09f7-37b1-89f9-cfd748113e7d | -7.24864 | -45.26431 | 2026-10-07 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 492690a2-bc87-3421-85cc-6a5a65534fc4 | -9.96424 | -43.48818 | 2026-10-07 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b33c3664-8d20-3011-bf38-91a560fe5238 | -13.20698 | -43.90295 | 2026-10-07 04:02:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8dcd6ea-2d0a-32e1-9900-3ec4179f2d98 | -11.62471 | -43.67406 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be724eb8-d81e-3ae1-ac0a-bf5f33eb7ca9 | -14.25267 | -41.6202 | 2026-10-07 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 79878019-f83e-3226-8828-27389c15e181 | -13.38571 | -43.87503 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b80d1e4-c401-3b5b-be8e-9f20675ee598 | -13.66719 | -44.3059 | 2026-10-07 04:02:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39681672-650a-30be-b0d9-aa8500d3ae03 | -13.50251 | -44.37154 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3b4688fe-ab1f-3a1b-9cb5-22795a528ad8 | -12.16727 | -44.17113 | 2026-10-07 04:02:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9793d7a3-4a14-3534-a5fb-24f30952629d | -9.2571 | -45.64417 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 723b4e65-474a-3130-a3ce-e05df2096e1a | -10.48499 | -50.43256 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0cd97d9-ac5b-3c80-bc0a-fcdc4259261f | -10.85005 | -50.65575 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32465a3d-8699-3b2c-b527-108395e6e365 | -8.20407 | -46.35663 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1e9fe82-2e89-39d6-abcc-bb0588c3ca45 | -8.28026 | -50.27824 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| efc456e6-a88c-35f7-b923-31ed854fcec7 | -15.00056 | -39.73797 | 2026-10-07 04:02:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6987df0c-e72f-3e42-a2a3-5d5835586120 | -11.73281 | -43.64898 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d00333c6-c71d-316b-8fb1-571743dc8191 | -11.2349 | -44.87462 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60fd8df6-eeae-39aa-9107-12f5299399da | -13.504 | -44.3635 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54abfc18-e4c0-3349-adbc-c581e709c725 | -8.44778 | -46.41144 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 700a4ad5-06c7-3cee-893f-bd56b89e0603 | -11.57908 | -48.59613 | 2026-10-07 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 732cdcaa-466d-3064-aa55-f4f8416b4813 | -11.37692 | -46.69425 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc116764-a20d-3956-a8e1-4a526147f742 | -11.74504 | -44.93963 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4427ae10-b7d0-3f08-9251-dd6a7b047110 | -8.69702 | -45.22141 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README40.md)
