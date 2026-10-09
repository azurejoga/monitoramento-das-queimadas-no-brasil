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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1283ee36-6ef7-3ab3-b6ab-5745792839f0 | -3.00218 | -54.77008 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1383fbc2-e1b1-3ef0-a3e0-7c6858df250e | -6.13184 | -55.68668 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d8aea47-88b9-3651-902a-5e369637d3dd | -2.97383 | -54.03593 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 197cd9e9-4c7b-32ac-879b-22fa0d255e25 | -11.64152 | -43.69862 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15cbca1f-fe3f-3bf9-ab4c-2a321898b3b5 | -8.70325 | -62.41189 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a4ff0ff-f565-3e47-83a9-a21cb034415e | -3.09091 | -54.29493 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70341754-a8f0-3b59-a7b0-85618c765225 | -3.03631 | -54.09617 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67436a8e-6538-32ee-880b-978cbeda7d0b | -11.27525 | -45.19201 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd66a20b-a93c-3e50-8bc8-eaff021c785e | -9.08296 | -45.10954 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da0a77a4-0b9c-3da0-b51b-45a71b094a46 | -8.17125 | -46.38908 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2150480b-3db7-366a-b138-41277a31c35e | -3.26391 | -54.00535 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dee8eee-53af-3e76-80d6-d9a04216b555 | -6.22708 | -52.79635 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c834973f-9b5c-3b2f-9606-db5b9e5ec448 | -5.0861 | -46.13403 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c989f4-e8c5-388c-a40f-d4ba79ae1c6f | -4.36428 | -55.20166 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 062d23ae-df3f-3228-b7fa-36697356a324 | -3.09349 | -53.94075 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 815b167d-e16d-3023-8cef-62723fdbe66c | -2.98411 | -54.06117 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5d123c3-0d96-3d0b-bc33-4461d3ddbd47 | -11.31626 | -44.83161 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3fd76e9-d303-3c7d-a524-7e77c9312661 | -3.01336 | -54.06098 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0651bfd9-59ad-397f-a6e7-984fff2b346f | -9.04867 | -47.73874 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af7aac8-90db-3378-88ae-393c708a9d9b | -3.45683 | -59.57006 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a48b3817-8730-3707-9401-e4c1fafd8985 | -10.74661 | -46.59366 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| beba6919-b291-3d73-ae08-f56e5107c5c2 | -11.46158 | -43.38508 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be4c667-2a65-30dd-8026-07f0aefde067 | -8.97099 | -45.91248 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc394e94-120b-3d02-add3-e7a658c7dd00 | -3.5668 | -54.67131 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 448d97ac-c823-374a-a882-1dfb9098655d | -5.98386 | -55.36165 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 963535c8-9844-3282-bffe-7f106d9ac403 | -10.94815 | -50.69187 | 2026-10-09 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d89b368-f5d0-3ae0-9c30-09b3db7f52b7 | -8.32588 | -45.44883 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fcf584c-4762-3367-be95-80594011fcd7 | -5.99918 | -40.96742 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 74f0860c-ac75-328b-8e28-151995af8a35 | -11.07611 | -44.0821 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 995a1a5e-f1cd-358b-80da-41b12d2864fb | -3.50561 | -59.27811 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ba33013-2dec-37a0-ba51-03cd3b81c8b4 | -11.64061 | -43.70616 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2df0b2b-f388-318f-9017-9b4df1c95d47 | -3.57976 | -54.68159 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a91c633-19d4-3c7e-8874-333333ebacd7 | -6.14301 | -47.92312 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b545cfc4-49f6-3b1f-b523-6ade87d7e6e6 | -4.08612 | -48.96155 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56df64ab-3cfb-33ce-89ac-aa48597202b6 | -11.72436 | -43.63392 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c70fe87b-494d-34e8-ba05-af1678c10995 | -11.7561 | -44.92731 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7497946-111c-31cf-829b-5a76a9fd574f | -7.44101 | -63.55124 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a359e5-f6e6-34d4-931b-ae478dce80d2 | -3.29927 | -54.00708 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cac14b1-9239-3de8-a663-a8d50c48f40d | -3.1103 | -53.76961 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14133a4b-44d2-3eaf-b186-5ed985e80c5f | -5.26694 | -55.95828 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a79ce81-bd1c-32f2-9e41-3ba01d812877 | -3.08984 | -53.96356 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06812729-7836-3612-8bf9-925c1ec5fad4 | -3.83085 | -59.41188 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f070fef9-6563-32ae-98a5-f092838e679d | -3.18784 | -58.65525 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31e56110-4b2a-37ec-a54b-f5559c656c1e | -6.13255 | -55.68244 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ad55d48-282b-3d64-beaa-ac5ca1b954ef | -2.5551 | -58.02921 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a85d3865-5f8d-397a-b0c9-f4b0437dfe42 | -3.29519 | -54.01035 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f25e26e-d67d-3be5-92cf-8639ecbdf656 | -3.00158 | -54.06395 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08afb004-0c2c-37a4-acd3-6e137bcfe535 | -5.99689 | -40.93778 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6832d5b7-1273-3632-9f8a-2390dc6f2272 | -2.98707 | -54.76486 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76357e11-6762-3fa8-8850-c55938f5a4a5 | -4.51905 | -54.89734 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6c0c06e-4461-31d7-be35-9d67589df169 | -3.08185 | -53.94672 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d79d91c-d87b-35a2-866d-689d18f2c8f3 | -9.89402 | -44.79186 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63784e32-ad3b-36be-9904-ed3353ecc058 | -3.36398 | -54.7449 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9e74f1-3cac-312a-babf-1a03fe9ddd3b | -3.14072 | -54.36739 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48e16b44-941c-3b5f-b69d-0a33910f7c8e | -3.59964 | -54.58218 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78d89f64-3b8c-386e-a7fa-ba3102ca903e | -2.99634 | -54.14217 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c7c90b-c086-3687-98f6-d0ee322e07a8 | -6.01672 | -40.97867 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f8de0b8d-aae5-33db-acc9-e4130c2b60dc | -14.05241 | -43.82743 | 2026-10-09 05:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aef8bd7b-16c6-3a1e-b507-2c522bd264e7 | -12.2136 | -57.09883 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d6f78c53-fd2e-39c9-a4f2-b6f6d4622786 | -13.41234 | -43.72798 | 2026-10-09 05:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 553ebc7e-cc7a-301f-99d4-39c8df2c809b | -13.17086 | -54.34835 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 695da871-cf9b-3f74-88c9-8e5bc92980f3 | -11.97078 | -57.59215 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eaaaace-3a0f-3128-afe8-8f11aec71539 | -14.73562 | -48.21586 | 2026-10-09 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 502521b0-5c25-3226-a80f-3ea2cf750270 | -11.79226 | -46.80458 | 2026-10-09 05:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39cbfbb2-b765-395f-8419-637a7180b060 | -12.22738 | -57.0837 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93c441eb-910f-302c-b90a-0158ab6d67b1 | -11.75174 | -61.0757 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dd45828-3486-30ff-b0c2-4fc1a23ab508 | -16.28517 | -48.01865 | 2026-10-09 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94bf300e-b8d5-3cd8-8af5-d0ba9bdad282 | -13.26295 | -43.99777 | 2026-10-09 05:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b1bc29c-2725-3f1f-a124-e44766f6fbd5 | -13.16151 | -54.32129 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c2e829-9fbc-3fe4-95af-2cf78d971355 | -16.58379 | -46.76136 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 152b4a3e-fa3c-37bb-afe2-f3b4bc4e9c7c | -11.97432 | -57.61613 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbfbf798-808c-3e8c-b570-01247959fca7 | -15.10722 | -43.63016 | 2026-10-09 05:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e2f0491-5785-3b7e-9742-58afdc5743cf | -15.25349 | -42.36704 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 376d4e3c-21af-338e-b56b-4ec7653ae614 | -12.22814 | -57.10134 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cace9181-2f43-3398-ace9-8dc5715a2e49 | -11.75541 | -61.064 | 2026-10-09 05:06:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 700360e1-065a-3a24-b7bb-9e0fd05ca0eb | -12.23902 | -57.10332 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ccd6919-5906-3bb0-8024-26d565be8f1b | -10.85177 | -59.11311 | 2026-10-09 05:06:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 197ac969-a3a3-3d89-9dfc-541419ef959d | -12.19762 | -57.12674 | 2026-10-09 05:06:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d94f300f-cb4c-344c-834d-7977e456a3a8 | -14.87442 | -50.30032 | 2026-10-09 05:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 48d313f4-8dc9-334e-a71c-83b43e8491b5 | -15.56351 | -44.51762 | 2026-10-09 05:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30a63e00-ebd3-3f02-9b66-efc97a3b40e9 | -13.20912 | -54.36566 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e6b23e2-194c-3674-9ec5-1b6a46778017 | -9.5338 | -63.56488 | 2026-10-09 05:06:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2b91383-746e-348f-975f-6353cbf1b6a0 | -11.90156 | -46.565 | 2026-10-09 05:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a799e888-832f-310e-8a8b-9e6e09e525ce | -13.1581 | -54.34259 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 364a161c-103f-3fc6-81f9-4e561009ed5e | -11.76051 | -58.28732 | 2026-10-09 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 422ef0a2-1f88-3a3a-8089-ff7b5b9d311d | -13.20302 | -47.86815 | 2026-10-09 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d059c51-683d-3c26-8ea3-0f0f42c4a1b7 | -14.01113 | -48.76541 | 2026-10-09 05:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5969d6a3-d98c-38ac-93f7-933e500b9601 | -15.71497 | -50.01043 | 2026-10-09 05:06:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a71b67d7-9e6d-32be-8f24-9e37d08bf5df | -15.34206 | -42.77507 | 2026-10-09 05:06:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dd5ead5-3acb-3d51-a27b-50820c81d512 | -16.58871 | -46.76205 | 2026-10-09 05:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eccbebf1-3a79-364c-bf0c-b6e898bc02b5 | -15.25229 | -42.366 | 2026-10-09 05:06:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 34e8c23c-016e-3fae-a069-747da110027e | -10.24804 | -59.0248 | 2026-10-09 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2abad1c-f5a7-34d4-8fdc-2949bfa130f4 | -13.20075 | -54.37522 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e47450a-83d2-3edd-9d3b-1451da0a635d | -10.38473 | -57.77658 | 2026-10-09 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e4339a9-0031-3749-82c3-85d1c2b670cb | -15.56092 | -44.51163 | 2026-10-09 05:06:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 941a7e7a-167c-3437-89eb-679354bf2cfa | -13.17971 | -54.35712 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b7b0447-fe35-35d4-8471-76e2897bb3e2 | -11.91088 | -46.56654 | 2026-10-09 05:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdfd2a84-009c-3999-be03-e31adf9c60a2 | -11.38686 | -55.09354 | 2026-10-09 05:06:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3a55e31-58ab-39e1-ae0b-d8a50004a5a9 | -13.1858 | -54.36178 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28a15320-3225-35ef-bc7b-344279187676 | -13.15867 | -54.33904 | 2026-10-09 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README172.md)
