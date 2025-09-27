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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d35cac-2145-34f6-9d13-343e9bf0a4ea | -12.6498 | -48.1509 | 2025-09-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| df2710f3-564d-36ad-b47c-916d58b75bbc | -20.5842 | -57.1587 | 2025-09-27 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 75008f5b-edb4-3549-8669-78f9a26a768d | -11.385 | -44.9386 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| bd3a24df-4a78-33e8-bfdd-c6c54166fc4c | -11.681 | -44.4312 | 2025-09-27 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 4c74d9b6-c0c2-3dbb-9526-1bedbcaa6318 | -5.3693 | -42.3077 | 2025-09-27 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 213.3 |
| 67fb801a-1862-3f44-998f-a810c51cfb9b | -4.1761 | -44.2716 | 2025-09-27 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 74caecee-7704-3a29-95d8-b1e637deeee6 | -15.4328 | -48.2126 | 2025-09-27 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 663c3b90-b63c-3c9c-aef9-5cd515c6ccd8 | -17.1736 | -56.4099 | 2025-09-27 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 72aff640-bc0d-3b09-833d-450db57b933e | -12.8839 | -62.1256 | 2025-09-27 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 96510a9e-1caa-32be-8c92-97f6a97fcc60 | -6.5163 | -54.8784 | 2025-09-27 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1ff0ea11-e863-3e60-95c1-1bdea2e0e6ae | -10.8055 | -45.3637 | 2025-09-27 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7c011c87-c868-3b0c-9619-ad751dfd93c1 | -18.3247 | -57.0913 | 2025-09-27 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.0 |
| d755a892-101f-37cf-8073-d6cd98a6f93f | -12.2829 | -44.0568 | 2025-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ea6b61c1-eb9a-37a2-910b-52e8898d1b8b | -12.6499 | -51.6584 | 2025-09-27 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 19f0e464-0469-32f9-b9a4-2659e0a97bd3 | -13.6316 | -48.0758 | 2025-09-27 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1419d5ad-7f53-31e7-8fdc-b25bc8bb4605 | -9.386 | -46.4201 | 2025-09-27 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fd9f1d6a-7905-332f-9b35-e217820d295e | -7.6252 | -47.3261 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a2634c80-dfd9-326c-a7fa-494ea5b40b8d | -9.0391 | -45.5334 | 2025-09-27 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f602c9dc-5d31-3850-8681-9fc0d12333f3 | -10.8051 | -45.3866 | 2025-09-27 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 00920522-ea5d-31ab-8027-fd1dbf083e9a | -6.2501 | -42.4736 | 2025-09-27 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| ce521d0a-c7c4-3f86-b994-27d84aabb0cc | -17.1739 | -56.3892 | 2025-09-27 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 91df46c5-3ffa-3d41-8dee-9682ad71b434 | -11.4417 | -44.9767 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 5491c622-a96a-3691-a6f7-5920ad33e264 | -5.3695 | -42.284 | 2025-09-27 14:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 9cec1098-7e74-377c-8663-c07cb86424ee | -10.2223 | -50.2448 | 2025-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 20da3069-2d26-3874-a10f-b1d8572f40dd | -10.9349 | -50.6612 | 2025-09-27 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6949ed6a-ac70-30d6-b8e6-ae266609c70f | -3.8277 | -40.3373 | 2025-09-27 14:30:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 123.8 |
| d9f2af68-6cbd-34c1-a210-4bb213238579 | -11.4221 | -45.0025 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 568454e4-bd53-37ae-8bce-35b07f08dea5 | -9.4269 | -47.5943 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 055a9ddb-3d54-3180-898e-13bdadd9a3f1 | -5.6813 | -43.0619 | 2025-09-27 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 234.9 |
| 0397dfa8-8156-31a3-ae83-0a79b2781732 | -9.3514 | -47.6022 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| ea90352e-da1a-39d5-b0a9-5fc466cdc6d6 | -6.6986 | -42.741 | 2025-09-27 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| b3e1f6f4-e56e-3103-881d-d5a3ac54b6f8 | -7.6399 | -45.9907 | 2025-09-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e153d9c7-0d85-3e92-bf26-ad9bb2de42cb | -9.3343 | -48.9364 | 2025-09-27 14:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 1c099165-1781-3c06-9cc7-078b39a69366 | -12.9722 | -46.2617 | 2025-09-27 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ca28cb26-c632-37f2-8012-05ceb1d13124 | -7.6064 | -47.3278 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f40967c2-e23c-34af-af55-7f25efcd3e53 | -5.8151 | -42.7931 | 2025-09-27 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 237b286c-2cdc-3fe6-b789-26d32c6d03fb | -9.8971 | -47.7421 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 35b1bea5-12ef-3dcf-a5eb-7b0108e1faed | -12.3776 | -44.1355 | 2025-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9e643f7c-3198-34f7-9ed2-55b021d137fe | -14.8304 | -45.3947 | 2025-09-27 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 474f9d83-fb3c-3760-80dd-3b784f64acae | -12.9028 | -62.1244 | 2025-09-27 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 034dae5b-d485-364d-9219-418242125163 | -12.0369 | -47.0543 | 2025-09-27 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| afacfd42-ac55-3031-b564-157b24eb612e | -9.3702 | -47.6002 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 657a213b-3152-3568-807e-fa5a5b0b0176 | -8.4825 | -47.8421 | 2025-09-27 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| d5b2cdd8-dbcd-34f4-918f-cec6281afb21 | -15.54 | -44.3169 | 2025-09-27 14:30:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 93.3 |
| ec318368-e261-30f6-a40b-053fed3de4e4 | -10.8242 | -45.3841 | 2025-09-27 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 791fe0e6-3d61-3b09-bcdf-0e3ddceb55f3 | -9.3511 | -47.6243 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7c218605-079a-39b8-b916-8de6078356e5 | -15.5394 | -44.3407 | 2025-09-27 14:30:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 72.9 |
| d27b1fc2-4fd9-3771-9cc1-d27d0fb7ea39 | -9.6159 | -47.5741 | 2025-09-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 36630ec3-f32e-383b-90b0-630f3483eff5 | -10.4025 | -48.1256 | 2025-09-27 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f0503125-7db5-3fc9-9121-819b6b3dca1e | -22.6077 | -49.0351 | 2025-09-27 14:30:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 116.8 |
| febc5534-043a-39ae-9b99-5577ec8032ce | -11.365 | -44.9876 | 2025-09-27 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 44e716a9-2535-3a2c-b5ad-4f9ffb8a8e5d | -8.6631 | -43.991 | 2025-09-27 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 27accbfc-8e3d-32ab-afd4-1b51a08e5caf | -12.6495 | -51.6797 | 2025-09-27 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 7f18952a-6792-3677-abff-20fb48c9a991 | -11.3646 | -45.0108 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 8d3f4ed5-c18e-3d20-b6f6-2c0ddaeccecf | -7.7797 | -46.9149 | 2025-09-27 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d1278478-8691-3e52-88ec-efe2e929e6b8 | -6.698 | -44.5774 | 2025-09-27 14:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e30d21e5-fbf3-33d8-8c6e-d0940b2fa276 | -12.3771 | -44.1591 | 2025-09-27 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8cc0fe82-d00c-3b1e-b21e-2b092ad92060 | -13.7109 | -51.1861 | 2025-09-27 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2b807775-601b-32d2-81d0-e0a228c6003e | -5.1887 | -43.7263 | 2025-09-27 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ec2af10d-3fae-3544-adce-0bb2fa15775b | -20.5644 | -57.1405 | 2025-09-27 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 2605b1ff-1375-3f7d-a7ce-48c00778a5f0 | -11.3642 | -45.0339 | 2025-09-27 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| fde2453f-9a1d-3c57-97a2-8bf1400d2643 | -9.9461 | -46.9385 | 2025-09-27 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c3e6d6b9-a2ed-365b-aa29-b315a7b7a723 | -11.7006 | -44.4049 | 2025-09-27 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0f00ee04-77d5-3bab-b5ff-ca93a3b8b0d2 | -13.3379 | -47.2921 | 2025-09-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c90cf6ee-5cf5-3ac5-996d-5992821b5182 | -8.1619 | -46.3451 | 2025-09-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 43f45c02-66a7-3b99-b401-194620455d6a | -11.4409 | -45.0229 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ec98bfeb-6282-3b94-88b7-d85b41ee279d | -7.1571 | -45.5158 | 2025-09-27 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 0d5fe10a-bcba-303e-acf2-d1ee35ab3e21 | -14.85 | -45.3911 | 2025-09-27 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 8372e8c2-56cb-3ee3-b38d-e87b4347677e | -11.0125 | -45.5189 | 2025-09-27 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 601080e5-3c9e-3428-9b26-640021f3dbf9 | -10.2409 | -50.2643 | 2025-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0e32de28-b6fd-3ed7-b58c-7bd161030825 | -20.564 | -57.1616 | 2025-09-27 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 289.3 |
| e193943e-e47f-33a5-95cf-953d8ba80c36 | -5.8149 | -42.8167 | 2025-09-27 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 464fb977-451a-395a-aa2b-f48c6447c48a | -11.4225 | -44.9794 | 2025-09-27 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 18955f18-a627-3ae2-8672-bff01e625c13 | -12.2632 | -44.0834 | 2025-09-27 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f96c4a60-116e-366a-a46d-45c421193d28 | -10.2223 | -50.2448 | 2025-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e1e4924f-3fac-343c-b978-99a4339c3596 | -9.9461 | -46.9385 | 2025-09-27 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 7d0b9631-b331-3737-ab43-f553b97e0bda | -7.1383 | -45.5174 | 2025-09-27 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 69afa3c8-3e24-301a-b020-c7f5f71e8587 | -9.3511 | -47.6243 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 4d0449e8-fb06-3442-9b40-c9f1687b2cf2 | -7.7797 | -46.9149 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 58bd119d-5949-3ccf-ab0e-0a64619a54bc | -7.6064 | -47.3278 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 25a66259-8e0f-3d5e-8dd7-5514ea36befa | -20.5842 | -57.1587 | 2025-09-27 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 0d1363ce-359a-393f-bcd0-10bfccdb400d | -15.4328 | -48.2126 | 2025-09-27 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 726f813c-c21b-3a8c-b730-6249b16491ca | -11.0125 | -45.5189 | 2025-09-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b9cca747-7401-31c7-8555-0020244b23bb | -11.365 | -44.9876 | 2025-09-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| af99f46e-4a61-36af-a862-45823852a8c8 | -9.3519 | -47.558 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d632df09-5079-3d7b-840b-3417f5bd2727 | -11.3642 | -45.0339 | 2025-09-27 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 59921538-0ecc-39ee-a843-f71c38811ffa | -20.564 | -57.1616 | 2025-09-27 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 30ad7786-ea9e-3637-983e-a99fccc0a680 | -20.7131 | -57.8321 | 2025-09-27 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 561c7959-ec22-31c7-b55a-01feadca10cc | -9.0422 | -46.7255 | 2025-09-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 472561ad-c997-3817-9ef1-a172fa526160 | -7.798 | -46.9576 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| de23b70d-b74b-3fa3-9dfe-cc87b6c0eb4f | -9.8781 | -47.7441 | 2025-09-27 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d25ac83f-bee8-3474-824a-1179679840c3 | -7.3849 | -47.0157 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 646a64d9-608e-3e9d-9c64-8ba36bcbbae9 | -9.386 | -46.4201 | 2025-09-27 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 66346005-3c84-3144-8e71-fa27136c314f | -17.1736 | -56.4099 | 2025-09-27 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| c6cb99b3-e4b7-31f8-95ef-c90f4e84e94d | -7.7609 | -46.9166 | 2025-09-27 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a87b7650-7ec4-32fb-be40-209b03a93170 | -17.1739 | -56.3892 | 2025-09-27 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 83bec2da-7f23-3dde-83ab-a01d6833602a | -11.3646 | -45.0108 | 2025-09-27 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 20005dff-7571-3ea7-8fdc-1afce67a1e4d | -7.3771 | -44.3096 | 2025-09-27 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 727e5e43-4dc9-3d40-a326-741fe3bf4e0b | -10.2034 | -50.2468 | 2025-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 261e647e-a8f3-3e9d-8a48-729d4eba195a | -15.2136 | -56.0047 | 2025-09-27 14:40:00 | GOES-19 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 284.3 |


[Clique aqui para ver as próximas entradas](README71.md)
