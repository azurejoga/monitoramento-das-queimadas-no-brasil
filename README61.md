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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3960e9a-3f3e-3638-9437-bd9ebe3cc049 | -11.77785 | -50.44008 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38cc5f8b-cb25-3add-9770-535b8d0af957 | -7.9815 | -45.65114 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf2b5a2b-77e8-3778-b825-d5f7672944c3 | -9.00505 | -47.03727 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36e675b5-9f00-3b38-a3df-6871f0642943 | -10.72736 | -44.77207 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9373cf3a-8677-3e1d-abf6-31a32ebc4129 | -9.04954 | -45.72366 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14bcdf4c-2855-3160-bf0d-9b0ff933b476 | -9.69296 | -62.00267 | 2025-09-15 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d08009e-d5b1-31bd-9395-e072061505f4 | -10.93171 | -45.59608 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9801e009-48ab-385c-943e-2dd868e9610e | -7.63962 | -49.74768 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d66ced0-da1f-36fb-8c37-f527a7bed0c1 | -7.64274 | -49.72564 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f2743b6-8cb5-3dec-b595-b03bc53a8ff4 | -12.44735 | -44.74799 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ae96da8-01e7-3b3c-a657-0ab2a536cccc | -8.95011 | -46.04298 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0509b6d-e118-3ef0-94b7-15b89f29e68a | -9.04989 | -45.72252 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79da1c4a-e7c8-37b8-b262-c68a71116338 | -7.85579 | -46.11931 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a87c5e72-919c-3da0-a2fe-557b1f86f732 | -6.62858 | -51.00313 | 2025-09-15 05:10:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e328ebc-4d74-30ab-9c94-53c3d498de24 | -9.14611 | -61.16012 | 2025-09-15 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77fa99fa-ed84-3e5e-83d4-7037ba197a1e | -11.4434 | -46.93205 | 2025-09-15 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4e874b7-3cc0-3f9d-9a16-ef50d88e752d | -8.92818 | -54.4492 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e96d94f-2264-3bb3-b230-837ef6dabb6e | -11.72206 | -46.48695 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38bcc9e0-55e1-3891-a6b2-1bce6d522481 | -11.0764 | -49.72568 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af82c3cc-8015-32d0-bdb9-f47a9c2e607d | -8.92286 | -45.47081 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 770916b5-6e8d-35a3-ba90-caef51013d05 | -5.76694 | -52.36879 | 2025-09-15 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192eefee-4b94-3338-b445-10a2ed50a795 | -7.98531 | -45.67188 | 2025-09-15 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45c19433-bf9a-3e0e-83fa-e13c29b3634d | -6.97356 | -44.55318 | 2025-09-15 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90f3e1c9-5e77-3853-8d2e-399b20860695 | -8.97932 | -45.81116 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c31c4257-8965-3685-90ca-2a2362a33275 | -10.7867 | -45.98164 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb3b17b2-68dc-3e4d-9903-debddf91eac0 | -8.64838 | -46.3627 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3dd7eac-6277-3ad3-be2a-735dc24c74e5 | -4.03988 | -55.56987 | 2025-09-15 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e281b9-b476-363c-88f0-7f97fae3370e | -9.05019 | -45.71837 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 728b72a9-e192-31bf-a6be-f4f009ebc66b | -7.6765 | -44.49145 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d4078a-861e-39d8-8261-86d8ade97967 | -8.97086 | -45.82627 | 2025-09-15 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3ed5790-7d5b-37ac-afa9-f8ba0ca96be7 | -11.85659 | -50.53123 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb018524-4c30-350d-ae30-803c29774435 | -8.96948 | -46.21895 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 373bc65a-d1a5-3a2a-8ce4-393f88d72029 | -7.89055 | -63.69518 | 2025-09-15 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e807e90-62d8-327b-a3ca-8554d02ee745 | -10.73336 | -44.76828 | 2025-09-15 05:10:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34e9b76e-2826-3ecd-ac62-4f6c2a9c7227 | -10.17129 | -46.15167 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2945703-5be6-322e-9661-ef56514f1997 | -10.32106 | -58.73249 | 2025-09-15 05:10:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1485c7f0-4cba-3758-917a-5fc8cca67edf | -8.59932 | -46.35087 | 2025-09-15 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21f76f15-e26c-32c7-a45a-8e854b3bdcb6 | -9.12281 | -46.94373 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2064011-ef9c-3e57-9922-81770e17fc4d | -7.63706 | -49.73041 | 2025-09-15 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ff95c22-1acb-381f-b266-4a58ee10a32e | -11.08246 | -49.73342 | 2025-09-15 05:10:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51dbc85e-1885-38ae-9d6e-0968584f35b8 | -8.96882 | -46.22432 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1114da31-6b88-30ba-9126-148bd7c49e87 | -10.79256 | -45.98421 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fb17f76-1c95-31e1-89de-026998cdb3b2 | -6.9183 | -46.17838 | 2025-09-15 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4702f3a-5955-36cc-a99f-531781409e8a | -11.44465 | -46.92188 | 2025-09-15 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1826c108-8ed1-31dc-821e-8348494ddbdf | -11.01107 | -51.24901 | 2025-09-15 05:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88fc0764-5ab3-3663-8192-8111121a672c | -10.66325 | -46.23793 | 2025-09-15 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 41544f8c-3660-358d-8016-f6ec39b9d5fd | -8.92411 | -54.44678 | 2025-09-15 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef398ab-d265-3b59-a42f-8ba683b5ea54 | -8.19028 | -46.76686 | 2025-09-15 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1210c6a6-1fa3-3445-988a-ec906a4a949a | -10.88769 | -45.44661 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1051cdb-bab0-37f0-b2d5-8bd5dc2a0908 | -11.71629 | -46.48089 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a68aa29b-93ce-3b35-9959-fdb314f721ab | -6.44977 | -44.52361 | 2025-09-15 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61cbe5d0-d38f-3737-881a-356d6d01520e | -11.79069 | -46.65418 | 2025-09-15 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 617dc136-1780-3c7a-82dc-fef2c566ccfc | -7.67732 | -44.48503 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9361699-ad59-32fb-a29d-92b2330e5011 | -7.30206 | -46.57629 | 2025-09-15 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b8e953d-708b-3cec-bd6c-08f99a48e302 | -8.18166 | -46.76906 | 2025-09-15 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e98075de-4aa9-3924-b57a-d392a6e5d998 | -7.49004 | -44.68943 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1188186-76c6-3942-bde7-9ac4e030745d | -9.01271 | -58.98812 | 2025-09-15 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 573b9fc4-dcd4-3e31-8321-41903ec77591 | -11.87123 | -50.54593 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3fb5e16-2cc4-3152-84bb-a13dac645770 | -7.70154 | -44.67266 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 128e33af-0e22-3667-bfc7-65e913386312 | -7.69327 | -44.68286 | 2025-09-15 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7975a4f-2e48-3d9b-8a03-eb5864f63884 | -11.44007 | -46.90774 | 2025-09-15 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e9dc34a-842f-3a3c-b45f-f229ab8df8d9 | -11.79843 | -50.43704 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c60d341c-cb77-312c-bb2f-02d2890540b2 | -10.79852 | -45.99005 | 2025-09-15 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 44f75665-e78d-31c9-832b-0b65904441d7 | -9.00302 | -47.05338 | 2025-09-15 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60528a4e-29e7-3814-a204-2fcab8e04034 | -7.92926 | -61.52972 | 2025-09-15 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c664a3f-0c25-3e2d-a379-993e0e668d76 | -8.96583 | -46.22213 | 2025-09-15 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3364938-6268-3f5b-a62b-9407e373e079 | -17.40566 | -49.26357 | 2025-09-15 05:12:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ef7d25b-0097-3ad8-8338-372e9c3c26bc | -14.81911 | -51.62935 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0f8b2823-7ea9-3e9f-a3e1-ba80b7d15d8e | -18.61802 | -50.39414 | 2025-09-15 05:12:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5502d5ac-1ddf-3174-8c99-dd8387412d26 | -15.90863 | -49.96645 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca44ae11-a003-38b1-800a-5556ae1a66b5 | -11.70267 | -59.31298 | 2025-09-15 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69a4cca1-8442-3d58-824c-770f7c17e4df | -13.00608 | -47.97571 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0e217fd-6f13-361d-932a-53b72b346f77 | -15.07956 | -52.46517 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d910fec-3be6-3d6f-972f-0bdf47ad0dae | -12.78148 | -47.92962 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85bf5d1c-4736-391d-9b8d-cad2e47ab717 | -12.79075 | -47.93079 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfcda8ad-79c2-3730-81fa-a681a854ef54 | -18.57778 | -48.1543 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d92355c-d406-3747-a27d-10c02e7ecfed | -12.43829 | -63.88604 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 609d728c-c522-365a-a6f3-a0de2473eb6d | -12.79172 | -47.94468 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7aa5118-4971-3234-a197-da2070e57992 | -12.78568 | -47.97596 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b216224-c808-399c-b481-2b10ce61d0d4 | -14.80202 | -51.61104 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| e422124a-13b7-3d0f-a6f2-afadfd855b88 | -16.66837 | -49.76936 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2c7192e-b00f-3317-b78d-ca948d0ff106 | -15.85219 | -59.40446 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e70883c2-66ba-3bc8-bd08-de07638bd0f7 | -14.94507 | -46.58305 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 712e0bd3-6576-33b2-9e4e-19dc0dcf67e9 | -16.67849 | -49.77935 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee1118b4-c9ff-3717-a73b-29ca32f6172d | -18.16378 | -49.20505 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| aa9e34e8-f060-35c4-873d-0459a56d6b4d | -12.78201 | -47.92513 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab4a162d-6696-3871-a0a7-fdb47af111ab | -16.71921 | -54.94782 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5948f66-0f9a-3c84-a004-df589d67400e | -12.40763 | -63.89185 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68cbcfc6-725c-35a5-9525-ac3291f36060 | -15.80509 | -53.47118 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f281c88-276c-395b-8782-7f6af2a1e205 | -12.78871 | -47.94891 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8327ae9e-8d7a-3f21-9033-499afc2c0f80 | -16.67882 | -49.77641 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faadb57a-e2ae-37ab-aa5a-5b9a8f890bc1 | -18.58398 | -48.15571 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81680d69-3e1f-39c0-ae4f-ab2e5f969d4b | -16.58102 | -55.17097 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0d7e24a3-f5fa-3d83-9890-36ad1db107e1 | -18.47724 | -46.94458 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4e9934e-0984-35ca-89fd-c8a0e343f90a | -15.09569 | -52.48309 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31912a64-a045-3d8b-8fb4-3365cfd2a4ad | -17.83076 | -50.42577 | 2025-09-15 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fdbc613-2cd6-3b4e-8508-610d743459f7 | -14.82814 | -51.63804 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| dce56ab5-e28e-3545-9ae9-248c6325eea9 | -15.10861 | -52.48988 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bffa0e0b-6f48-3a4b-b4ee-a7e04922663d | -16.27918 | -54.92413 | 2025-09-15 05:12:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5890cdc5-36f0-3254-9ad1-2dd870e26fa3 | -14.79661 | -51.61779 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |


[Clique aqui para ver as próximas entradas](README62.md)
