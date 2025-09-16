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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3634522d-0189-31d4-8f50-52723b53216e | -11.49368 | -43.72593 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb3d3514-420f-3625-919c-fa00c17d3ce7 | -6.17868 | -41.21985 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f20bde91-2dbe-364c-be81-22a9ec4b72cd | -11.43418 | -46.93712 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a678cd8-3f0c-3370-b525-35544d322ee8 | -6.97818 | -44.54003 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bd93c5b-8d08-3d0c-83d7-4de4713d8ebb | -11.30351 | -50.85134 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2bf6502-3340-3976-90bd-e15292c6b76a | -8.59449 | -46.34441 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 096a089f-0893-3196-b146-46e905fda52c | -10.64551 | -46.45546 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94004951-9b04-3543-b223-0aaa988e0eac | -6.68371 | -46.30634 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cd5780ae-668f-3a74-ba3c-12971053ff65 | -8.92274 | -45.46434 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90144937-f0e0-3fe6-9110-bbfd9bf0b6e8 | -10.71023 | -46.51452 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| eaa2b356-2bbc-3343-8413-c15bd18e4400 | -7.52336 | -37.66745 | 2025-09-16 04:02:00 | NOAA-21 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a3b70a11-8c67-385e-bbd4-852c5037adc8 | -10.71761 | -46.4963 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cc8579c8-a8f0-3dc5-b960-6ce01c220a34 | -8.20594 | -45.5495 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cf199d1-776b-3c55-8fa6-7b318bc34d3a | -7.06859 | -44.15996 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8fa906c0-95b1-370a-91d1-3d66927c16bd | -5.34323 | -44.82991 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92b4cf5f-b4b6-3884-af5a-1371c80be573 | -7.83922 | -43.85689 | 2025-09-16 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83bf7da6-57aa-3c45-ace0-0eae20a5eab3 | -10.71499 | -46.51149 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 67adcc28-ba36-34f3-90f5-201a3e51c064 | -8.92037 | -46.11905 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbef03ad-7f8f-3d17-a446-7197b06f1e7f | -10.06077 | -45.50736 | 2025-09-16 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e82830d5-fd2a-3dc0-8731-6379a34a3861 | -5.79072 | -45.93718 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd4fd58-d4db-3072-94b9-1bca4f436d87 | -5.21044 | -45.18507 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ad01897-2f51-390b-ad2c-6c98081d6bef | -6.16997 | -45.11486 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b248d334-2bf5-3b22-a84c-5f5768283bfc | -5.3444 | -44.82272 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bc6487a-dd50-312e-8907-26e2dcec966d | -6.22433 | -43.90574 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06497b3e-75e9-378d-a867-0664df14fe42 | -5.19321 | -45.58689 | 2025-09-16 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2db1f66-9703-3bb5-9d31-c74072563bee | -6.83115 | -47.85254 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f282d9fe-885d-3222-9bbb-34f753221b15 | -8.89684 | -46.15706 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab5e1dc7-5c9b-3a03-9d6a-295cf69f064e | -5.38963 | -42.83686 | 2025-09-16 04:02:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8ba4a1f-55d5-3eb2-a0cc-1e851e6769dd | -10.72289 | -44.74551 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 46ab9925-d7d2-32a2-86c7-c00096d1c63e | -12.26894 | -45.29384 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7750476-a758-361f-85b2-aeadbc4e875d | -5.05315 | -45.19794 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b382193-cefe-3cfe-9c10-77118fe4aaf4 | -10.78697 | -50.66037 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9431f6fd-0305-3164-adb4-c75c47440404 | -6.1739 | -45.14147 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de3fea00-0a5b-319e-aed3-fae3bbf91ac6 | -6.28621 | -42.38617 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c46dcb98-a1b4-3c7a-9a1c-8d4fa468a191 | -10.72214 | -44.75009 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5b80197-c143-3b10-90c5-dc12c4cf6bac | -8.61407 | -46.38379 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a15191c-2d9f-314b-a6bd-91672c179aff | -11.51898 | -43.25105 | 2025-09-16 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b720477c-82ec-3652-8e60-017cc176cdda | -5.78705 | -43.89406 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 818a769a-1ebd-3a4b-a4cd-641f25a3fd8c | -7.55935 | -50.45987 | 2025-09-16 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f978e54-31ec-3354-92da-f138379f038e | -9.70222 | -42.7082 | 2025-09-16 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1ec95d77-ab7d-3d14-848d-f72e8607d1a0 | -7.69004 | -44.49298 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dd92d35-4acd-344c-aefd-0c83eab176fb | -5.8 | -45.93438 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adf641fe-b9d8-346b-a787-e8052a1dcdd3 | -7.31526 | -43.96099 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30cb10ef-db66-382a-871a-ad71c0d80774 | -8.97696 | -46.24859 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c601d8-ddef-3237-8420-172af7a68f3c | -8.41467 | -47.21584 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64f836a-ef5c-3c8d-b588-f4d073e2078b | -6.00016 | -43.69974 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14a8b884-9b0e-322d-849d-8b1fd4b3947c | -10.05264 | -44.34822 | 2025-09-16 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1e888f7-3365-3917-8de4-f5cd83426f91 | -9.04864 | -44.83204 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 323e6c0c-544b-3796-af80-c3d960ef8eb2 | -7.66957 | -44.47526 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54586913-3c45-3cd1-b754-020005e4e5c8 | -8.33309 | -44.74283 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 758c0421-999b-3b91-9070-ddee2c8ded00 | -7.31673 | -43.95203 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab35b503-e7a8-3ac1-a150-6f46a7ff4b30 | -9.06368 | -47.02386 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 76794b10-79ee-326a-992c-09c468c42584 | -6.33259 | -43.33619 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b03c9a6-d799-3e08-9ca0-63fa766ba7ee | -5.05728 | -45.19862 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2123a346-8f7f-353a-9a89-843641044d71 | -6.66699 | -45.54074 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b831031a-c008-364e-8f9f-9d3d5e59b6d5 | -11.97076 | -46.77806 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f861deab-3150-3dab-a9ae-572fac2e8291 | -10.71767 | -44.75412 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 74fe4ee6-63b9-3a6b-b8e8-9043ae0042a9 | -11.99298 | -46.67495 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcaf7567-8a00-3f1d-a2f4-75729bb6a30d | -5.80133 | -44.86234 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aaf203e-df4d-324b-a008-aa2f8e99bd3a | -10.71976 | -46.50836 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f5d79d-be80-3cc1-bbb9-1b890dff30c6 | -11.72835 | -46.48589 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62731491-8c5c-33d8-a893-e3f4d3d0292e | -6.41304 | -44.36766 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e9aece-87a2-30c5-859d-d4bc20a6a3a8 | -8.41994 | -47.21202 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2438d7d9-8af6-3194-9d08-087374f60c2b | -7.68927 | -44.49763 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90027cac-a68a-3602-95ad-8630d63caf80 | -6.35119 | -44.31303 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b48aa3a-d5ae-34a1-adde-aea593fb6de5 | -8.01 | -45.66624 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baa011ed-7075-3e20-a0a4-e9e8208cd351 | -5.66658 | -43.32326 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cf04635-52c8-3a21-8c58-94834d22e686 | -5.66922 | -43.49252 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eeddf60-b007-3197-bfad-74d7cb3bd5e0 | -6.52749 | -41.82533 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9a6f7c29-4c0c-3f9c-83cb-c5b17d5ef029 | -9.05925 | -44.83873 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fe49c49-5a0b-302b-9e1b-72e284aa0eea | -5.79082 | -43.94183 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0df51e3c-aa6f-3655-98ed-1ae8b0b18d28 | -9.05086 | -44.84217 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c492f44e-f2eb-335f-84d3-3deb5bfc4373 | -5.73957 | -43.92094 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecb922df-59ad-3dfe-87e8-cd36f016ae60 | -7.44097 | -46.17368 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3610b0ae-a456-3acb-a5fa-d1cc036a823a | -11.43766 | -46.94174 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e76bccca-8ed1-3770-8f40-cd3188c65151 | -10.44591 | -45.14758 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a353497-0c50-35ab-b323-6d8a1f92f18c | -7.56005 | -50.45588 | 2025-09-16 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57365315-e2b8-33aa-b667-db62b8295351 | -10.71894 | -46.48864 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e613e73b-0ae3-3f93-a949-f2698e5c1b5c | -5.79842 | -45.91746 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 763a7d80-522a-3dc6-a520-1f824f9aa774 | -6.18543 | -41.1991 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b8f48ca0-6dea-3d58-b7c6-16db735ad54c | -8.76646 | -46.08442 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33f765b6-2cf0-3c12-8ee5-492ac0ce081e | -5.8029 | -43.939 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 533dad91-a718-3238-9490-6cb4e953335f | -11.24163 | -49.95186 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5609e4f0-b8d9-35fc-8adb-0c884d6dcb37 | -7.26908 | -46.58925 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fbc3c969-9b0e-3f05-929e-74e165857e8a | -7.26967 | -46.6118 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b1b9371-9aee-3ed8-85c5-c671c19b7e28 | -6.34353 | -44.7695 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db1ba449-204a-30c6-a4f6-1b6c190a37e7 | -6.89481 | -44.55293 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9fbfaa-fadd-357a-ac1b-dceabd52a3af | -11.71455 | -46.87526 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ed09efe6-5b4d-3c2f-b369-c2a79c4ee661 | -11.46189 | -46.9267 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6960e1c1-fa44-3f61-ba50-f30408e1dbdf | -9.14644 | -46.94277 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78c528a5-7b70-3144-ad2a-590f2972f146 | -7.99713 | -45.66814 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f02c592-7b17-35c0-9f00-3a42c8ecdbe0 | -10.72358 | -44.76436 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cf573bbc-8aa5-317a-8af8-b162f44ed737 | -10.9202 | -42.84526 | 2025-09-16 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a6a5f89-ab0f-340c-9b44-80af4486ca1c | -10.63947 | -46.46613 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c4b5295-9ba3-3719-9baa-dc363c892326 | -5.86961 | -43.71714 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb8a2fa1-5722-38e2-bc93-197dfc0ba372 | -5.66993 | -43.48816 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12ca4ddd-6187-3e79-96ab-ff56e6c628fd | -7.45152 | -46.1632 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66d083e5-0f25-3ab4-b529-f5f823274808 | -8.97765 | -45.75853 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe2228f-b453-3fac-bb44-44d908d1b8de | -6.1666 | -41.17026 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| adb7a7fc-c51a-319d-9f33-3bc8ef7bf27b | -4.62922 | -46.12248 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README14.md)
