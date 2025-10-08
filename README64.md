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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b83c8554-a019-3e49-a93a-75270ab9589b | -6.06576 | -44.03545 | 2025-10-08 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8efe3aaf-91a7-3733-a5d2-af3ddf4c8087 | -6.69106 | -58.81326 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b754fd08-d038-36ca-a452-248d9057bab6 | -5.86887 | -44.30478 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60fbe706-5b94-3d5d-8567-b15ff943f4fd | -6.59641 | -59.11857 | 2025-10-08 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66259905-1367-3c51-95ee-0485248e5e6e | -4.6862 | -45.83294 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42f79959-c848-3209-bf7e-c0f40117abd7 | -7.67381 | -42.58026 | 2025-10-08 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3832460b-c0bf-3c7c-9d68-0284f2884b86 | -8.52271 | -46.28515 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06b66393-e934-3d42-8aa1-377d85e5a853 | -7.8045 | -44.22192 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 296a7db2-a0f3-3bcc-bfd8-e5842106687d | -7.82 | -44.17414 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80ff11e7-d09f-3312-aed3-55c9096f6888 | -9.67716 | -45.6764 | 2025-10-08 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c259b16-0f21-3447-84e8-ea22fd53d4e8 | -10.64271 | -47.79 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ffbc478-90a5-3962-a523-b381de887581 | -11.78499 | -45.14083 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d1036ce-3965-37f5-85b7-5f58e041287a | -9.19743 | -47.85644 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e90421cd-032b-3267-8f1e-27e18a32a6ca | -5.72246 | -49.30811 | 2025-10-08 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d550bc48-9d2e-3a80-ad2f-43f990f4e754 | -5.45557 | -44.17514 | 2025-10-08 04:38:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e477911c-cd5a-3530-a123-1347dbd28fdd | -11.08708 | -49.83706 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdfe50b6-977c-30da-90e4-db22aa0da3b0 | -10.38328 | -48.13334 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f5daa62-dc0a-3268-a028-024fb809dddc | -11.78085 | -45.14772 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7de9d7de-6523-3f1e-9434-76dfccc80922 | -5.85406 | -44.30694 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42e9fa9d-112f-3242-9296-6d9877230871 | -7.82079 | -44.18581 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 911f0f32-8031-30fa-b86a-91a83c23764c | -6.4214 | -47.237 | 2025-10-08 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d636875e-6ad0-3f43-8f7b-69615bbef5bc | -3.31054 | -51.51851 | 2025-10-08 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df5af85f-2313-3e5f-abc6-503aa976edfe | -10.23454 | -52.70063 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27e417da-252e-39ad-818a-092700b6c325 | -6.4946 | -47.49143 | 2025-10-08 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af265baa-0ddb-349b-86d0-db80cd4079bc | -7.79433 | -44.2051 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d886120a-e7e5-387a-b8cb-50637e56135b | -8.59513 | -44.90316 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2462975d-2ae9-33ad-93e1-a579d63c3b28 | -5.32699 | -43.80472 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8152964-06ae-3f67-9414-cfbb46df4bdd | -8.55676 | -46.23288 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60add8e7-dc49-3aca-a297-33eba413718e | -5.6478 | -43.18137 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3c21664d-b20c-32f7-b010-1e7eaef987d8 | -5.16546 | -46.22393 | 2025-10-08 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63a57508-2185-3526-a0c1-bb18235a9a3d | -10.47166 | -49.38509 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 977d7bd0-ad71-3eda-8e2f-2cffd031212c | -5.70646 | -44.21699 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57ca13c7-4d13-3bf6-ba01-2fab26e9b642 | -11.79049 | -45.0499 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 610900bc-e45b-3dd4-a29c-be06bca96764 | -8.41169 | -49.72529 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 795e68ec-7094-3e3b-8a62-ca96b8c598f9 | -7.7979 | -44.20949 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2d1d3ac-abb3-3720-ae29-54824b9af181 | -5.14211 | -44.96607 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 191783a0-b5f2-3f82-ad44-fbb3a7548552 | -6.71959 | -58.59172 | 2025-10-08 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e3d2214-5160-38c4-bbaa-6cd5592fb407 | -11.79064 | -45.13779 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d62dd4c-6265-3f28-98cc-f3f7f5b04211 | -11.68436 | -46.38167 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 024ee812-8a73-3c04-b8f5-7ee7a87a10b8 | -10.67877 | -47.552 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ebc354f-e772-306c-901a-83e6f51c1643 | -9.97923 | -48.30702 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f221554a-7337-31a4-8f6c-82927336f943 | -9.75776 | -47.69257 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b45435-8cc1-3c35-aea2-c51685626eac | -10.24285 | -52.69394 | 2025-10-08 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0452e5b-4e1c-339c-9821-8e226e1c77df | -8.56327 | -44.62831 | 2025-10-08 04:38:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38b1820f-20b1-36c7-8500-d910921ecbb8 | -9.45348 | -54.67034 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72c52598-3184-3e32-954e-1f7dd1f162c3 | -11.24258 | -47.38184 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc5db021-07fd-38b4-9a72-05ab065b6ca8 | -6.70557 | -42.86164 | 2025-10-08 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e63eecb9-23c5-3767-9776-e328a802d17b | -5.64022 | -43.60721 | 2025-10-08 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4c0e1a0-c099-3073-8cbf-f7c9b37425c8 | -3.83639 | -49.16236 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ea09d5b-368b-344c-b78d-e3a23b55f223 | -9.25996 | -56.28635 | 2025-10-08 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c00006-27af-3e56-862d-9abd5cdad6ba | -11.27515 | -49.01515 | 2025-10-08 04:38:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a6f443-30ca-3ed1-b7fd-85dbf504aad7 | -8.68335 | -47.07632 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edc75cfb-3ca9-3d94-8ea2-25cfd11781b4 | -7.24166 | -48.4798 | 2025-10-08 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3c688e2-5799-3f71-9395-8b21544f1b9d | -10.415 | -50.225 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14c97d2d-f63a-341a-a098-519f91754690 | -8.67628 | -47.07526 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7bab0f0-95a8-3ad6-be59-679b352df76b | -4.49667 | -46.3649 | 2025-10-08 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bb9fd0ff-7017-383a-8f6a-cef49008bfc9 | -3.81234 | -49.46397 | 2025-10-08 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6363e8a-b517-3851-b198-7fc899f4bb62 | -11.70747 | -46.35604 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8648315e-5bd8-3a1d-9be1-034bd7c1c5f2 | -10.32742 | -51.22466 | 2025-10-08 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bfd8787-3dfa-3bb2-a904-9535c0ce1bbc | -10.32685 | -51.2282 | 2025-10-08 04:38:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c3eecd9-71a8-3a42-8ca0-88f4b7d95371 | -4.68461 | -49.49129 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22a576f5-4af2-3613-b19a-b1650a04266a | -8.1102 | -44.77423 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deff68c6-5191-3f56-b1d7-a46bc3671f0f | -10.60203 | -49.63739 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ec0c38b-8c9d-39b5-9644-13a580176963 | -9.17853 | -47.81864 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf30753f-ecc2-3347-a8a3-600aa874b04f | -11.22185 | -47.76312 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ee88f1-2278-3624-a6b3-4281192687e1 | -4.68856 | -45.84158 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f853324-7101-3c87-b082-17d7a15b2054 | -7.72621 | -42.4109 | 2025-10-08 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 75a333e8-190a-3493-8d45-ca951ca2803a | -11.14081 | -47.74798 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fc8fb9f-8a15-3c9b-a59a-92fc473c98ca | -11.66359 | -44.25915 | 2025-10-08 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a6c7a67-ddba-34e5-b682-7ced8625f75a | -5.30017 | -45.84728 | 2025-10-08 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32fc0716-31bc-3a7e-9058-20b1cb2f0cb2 | -5.82055 | -46.74387 | 2025-10-08 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dd8d402-9965-3a99-b34d-0d0d0abaadc8 | -7.44693 | -43.13326 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b5678607-1292-36c5-99c4-9e7545d3373b | -5.71378 | -45.68717 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b7f558-cd50-3ae4-b893-586f0e088347 | -9.17999 | -46.91861 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38cbc030-9826-3c05-9460-ef4995b08438 | -5.71551 | -44.82817 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9cc32c8-0463-39c3-adf4-ad02a801e4f7 | -5.61457 | -43.93881 | 2025-10-08 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ece2ddf4-3a9e-3e01-b87a-0e1d573888ce | -7.45255 | -43.12533 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ff79f5e-6d57-3647-8fbf-5ab9caa41f08 | -4.05372 | -47.50142 | 2025-10-08 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f19e113e-6b54-3994-a957-36ab76fa4df5 | -7.43691 | -43.14047 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a50c9c9e-5c73-30ea-9008-03c658eccf50 | -6.22214 | -44.30057 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26d9cad7-b30f-3314-8634-17ceb1ce5e97 | -8.6196 | -54.99479 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c615de8b-2de3-35a6-9460-378a8e5e56f8 | -8.47335 | -46.29296 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6cea8061-8963-3527-a638-6f10c363cba1 | -11.49726 | -44.97106 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf70154d-5b96-3dff-87f7-f7e465076912 | -8.18561 | -43.33765 | 2025-10-08 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 6427bbdb-f79a-33ff-8b0e-f7580fc23492 | -10.38618 | -48.13737 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef964ccc-0a3e-3708-be49-8663c655eec5 | -8.92519 | -46.59347 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abe56dc4-4078-33ed-bc67-03467b46e143 | -11.46969 | -43.48887 | 2025-10-08 04:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96664072-ac60-37db-849e-e21d3ce72e54 | -8.61116 | -44.90504 | 2025-10-08 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cad36251-dabf-365d-a98c-63ba6271c113 | -5.70594 | -44.22047 | 2025-10-08 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 988403ae-d14a-3d60-9a51-947336f37d26 | -5.37505 | -47.777 | 2025-10-08 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b2a5a6-c144-3bb9-9ff7-bd81f9f24cff | -9.6399 | -55.13497 | 2025-10-08 04:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9259185b-3ead-33d4-a073-4919727cfdd2 | -5.16914 | -48.96276 | 2025-10-08 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a8a2843-18e9-3529-ad28-58f68ea3d61d | -10.36467 | -50.28464 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30fcbe44-11bb-3cbb-b6a7-6df04fe3d454 | -8.1062 | -44.77363 | 2025-10-08 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c51cfe41-0d44-3625-8a7d-da3398c6a60e | -11.80644 | -45.04397 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9976f14a-0223-304c-877d-075b43891fb6 | -4.50972 | -49.24412 | 2025-10-08 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14399ff-ecc3-3a6b-b9a1-f5126f36217b | -11.79986 | -45.04325 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62172160-9fb7-3bf3-b8aa-9f5d0a21e150 | -11.21716 | -47.77057 | 2025-10-08 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36a06fe7-483c-3d90-9739-14b68ff1562d | -7.82457 | -44.14325 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 302dd44f-831d-3e65-812e-b5dd4e228d4e | -11.7845 | -45.14444 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)
