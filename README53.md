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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5be4cd4a-8906-3ea0-967b-5d5d951b446e | -15.27217 | -49.29293 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c019cc45-a496-3c4c-8ac9-c24d52f56b35 | -12.92739 | -54.7253 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9568596b-4f2c-3aca-b6de-21feedf41d5e | -13.74096 | -48.68814 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a76f65ee-d9ee-395c-8bfd-56cba893ce9a | -13.66916 | -48.07294 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96168f4a-7618-3c92-8d69-cba4f0b26b19 | -15.17712 | -49.08221 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 517837a4-e18b-3c38-9bc4-3e37bd0abf94 | -11.13976 | -43.37774 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 55d22058-0e0f-3b73-a930-e25b38e0e194 | -13.23137 | -47.32174 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 081e9c57-7e57-346c-bb24-abc2ccabf678 | -17.6408 | -46.08883 | 2025-10-01 04:21:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87631b6a-7dc3-3665-b1c3-90d1d7074d88 | -15.1729 | -52.812 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47c54448-0a8c-3ffb-b46e-164426ff2cb5 | -14.69138 | -48.12699 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef5ba728-0bb5-3c13-9eb7-7806343b7b91 | -13.92169 | -48.1037 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 695adc72-27ba-359e-b605-0eebd06eb73a | -13.98147 | -45.05658 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b798e5e2-b730-38dc-923d-5356136c85b9 | -11.75692 | -46.8325 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baf04e4d-3972-3245-9581-231d96688bbe | -11.45254 | -44.97128 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afec51e1-b971-3c92-826b-1ddb55eb76c1 | -13.36178 | -48.10931 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b0fa164-784b-3e52-a37e-cf319e673ad5 | -12.92136 | -54.73035 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6be12b9-dee1-36d0-8cf7-aaf56f581e57 | -12.82898 | -46.98409 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d03df25-5427-34cd-9cf1-d7c22c765d46 | -11.83584 | -44.97706 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d6a41a4-4962-3805-aec2-114de1e66939 | -14.68066 | -48.12917 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2985353-a4af-3266-a213-ae4b3b575ff5 | -18.11762 | -42.73423 | 2025-10-01 04:21:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c82b973d-3ba4-36ca-8ace-200870ae31a6 | -16.06419 | -51.0125 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bd5cfb9-7b50-3675-866f-edb1bb7a825b | -15.48799 | -45.90154 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46d719fd-0a49-3fdb-8c40-4bb5a6b73eb2 | -12.41823 | -44.09404 | 2025-10-01 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc0446ff-927c-3e84-a742-9b815a88cbaf | -16.58829 | -45.12942 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b2d386-e6bb-3216-b413-be5c7ec0b552 | -13.92784 | -48.10852 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8f80d41-e00e-3aab-ba1c-e363f11ee6bd | -12.70067 | -48.55855 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5a2df94-7d27-33f9-9707-c0e341013885 | -10.34389 | -48.20161 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dab0724d-e87c-32ec-85e4-d0272cb8ed64 | -10.03742 | -52.09822 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a59fe801-3b63-30a6-bd30-fc3e89ed1b5c | -11.83693 | -44.96995 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db539274-0426-3d93-b31c-9a9f2a3252ac | -15.77656 | -43.68299 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f86eca50-54cf-3ed4-bff1-d6d119bcabf0 | -11.7679 | -46.84904 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f47fd7ef-8555-3e69-8bc3-289e962a9578 | -14.35483 | -45.93278 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bbb6906b-3633-383d-ad42-9fc08520527a | -12.00969 | -46.63432 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 414d2df2-8deb-3518-a1ee-0425ff96eab0 | -12.23401 | -47.8218 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d98b9f95-386c-3002-a652-5953ca10834c | -13.16136 | -42.35522 | 2025-10-01 04:21:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d54111fc-0cdd-334a-a1ed-b2227b824182 | -15.30027 | -46.19556 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78ee1300-5edd-3a8d-8d9e-d184e1e0b6de | -14.99058 | -46.96148 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 956fc743-7a25-3f74-9d98-f0d909d12e67 | -13.29467 | -46.38722 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bab573c-381f-3ad2-bac8-684bef3a373d | -14.71926 | -48.14668 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30abd7a3-20d9-3d07-98a1-8be450a12383 | -13.98102 | -44.87514 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae95a3f5-192f-35ff-b411-cb2dc3e9a409 | -12.91908 | -47.1669 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d38d36-986d-36d8-b42f-89348c9656a2 | -12.76617 | -46.90813 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89dae442-432f-3246-b028-0844a50e8b0e | -10.92814 | -54.33002 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64c43f5d-d461-3cb0-b838-5a66edb53d66 | -14.99171 | -46.95434 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7c63254-09ff-3082-a35b-a66c860af290 | -15.34662 | -56.95473 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283df852-0d99-3a0e-803e-81ce248c3199 | -11.84752 | -44.98986 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5bc82807-7110-3cb3-9d30-b9a67dde1980 | -13.74706 | -47.92266 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c211c36-fca6-3030-ada6-8f41203e7abf | -12.87623 | -46.90056 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 353ebd02-63cb-3542-8d04-181efd29906e | -15.05208 | -48.0674 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 471f46fb-5a8e-3ebb-95e6-ac6ca72ce2d4 | -13.94541 | -48.10716 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d11fbf29-6662-389d-b11b-150dbccd82b5 | -12.64048 | -44.22735 | 2025-10-01 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d25df1b-f4e1-3eb5-800c-7542e2770843 | -14.98529 | -50.76633 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfc5193f-f19e-3ee9-890e-49147afb9ef9 | -12.67134 | -46.86352 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b99bca72-28cd-35b8-9aff-54823cfe06d0 | -14.60475 | -48.22303 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f6da55c-0c8d-3dee-98c8-c753c8b52eeb | -9.58494 | -54.59529 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0789abb-3cf2-3b05-aa63-2a8c79375bea | -14.54443 | -48.23167 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39a2a2d-adf3-33ab-bb93-1f4395b44175 | -11.39645 | -44.8935 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f12a8b-2bb3-3e5a-af33-60f7361dc010 | -14.50576 | -44.85935 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0501e0b3-4cfc-31c9-b935-2b130e5be5e5 | -11.38188 | -45.05516 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b40bc0e4-91b9-3412-b105-e9a64e43dbcf | -13.96146 | -44.91366 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c67d5f75-f5ed-3642-8360-ae639e308eac | -14.50743 | -44.84799 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa57e7d4-d540-3d0d-b6cd-3eb039ed51d5 | -14.43913 | -46.35447 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 160b49fb-4d07-32bc-9ce4-3127ccb50ec4 | -9.51983 | -54.74374 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b522f56-a2fc-37aa-8d9c-46fe35a4bca8 | -9.5847 | -54.59781 | 2025-10-01 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 997b62d4-420e-3f80-a09b-c5ce1a10724f | -15.31797 | -46.41063 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fed87507-1c74-3f45-8eea-e92fc0f1af88 | -16.64816 | -41.12819 | 2025-10-01 04:21:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 339a88bb-83d3-347b-9fa7-fc15cc26622b | -10.82862 | -45.37719 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e6b85b5-494d-3bed-8dd9-99f6cd4505b3 | -12.83167 | -47.00993 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a88394db-388e-31a4-9d57-c776bc7e4949 | -12.93284 | -47.18755 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9523b58-e355-3bfe-b8ca-9b5d0ce76cdc | -11.09684 | -47.72256 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5cb6141-5a09-3764-af3b-0b08804a3dc1 | -12.70714 | -46.89472 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 143b1711-81b0-34df-a97a-6644c284557c | -15.18326 | -46.40331 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f18d4015-9728-3cdd-964a-3b49c45f4231 | -14.85617 | -47.05904 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb3d9917-566a-33a8-b784-6319c84f87ca | -11.46698 | -44.98827 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acf47ccc-3dd7-3871-9c34-868b68e0b20c | -13.94354 | -48.11858 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6a91b846-631c-3d2b-b52c-281bbafa5a24 | -15.48204 | -48.56033 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99538c0d-0772-3c9d-8a17-694bd173945e | -11.99987 | -46.58928 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ca3d00b-1cf7-38d0-a9b3-080b565613ed | -13.29543 | -47.58075 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5eabf802-326a-3081-9981-33528db48532 | -16.58543 | -45.12503 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36ee4118-92ff-3652-bb42-0b6d261d2f10 | -12.88333 | -44.6839 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 931347a3-15ea-3972-a019-375aaebfc0b3 | -14.80261 | -48.32503 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1b2951a-edd3-33b6-86f4-e182981ec9f0 | -12.88709 | -45.19355 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76aff438-7afb-3205-80d6-c5dc8710be86 | -12.94544 | -48.41665 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87506e84-881e-369e-b2cc-636807c79c33 | -14.13605 | -43.4633 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0628fabd-ceb3-3abc-9ba0-2374fcd5c9d0 | -13.07483 | -47.08691 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 688e5cd0-aa2a-3f0e-bcc7-b1006ec60c4d | -13.58039 | -48.04269 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dff53528-fcf2-32c5-96c0-b283d8044a5a | -11.78382 | -47.58072 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ed24d44-0826-3810-bd1b-a26d21e56566 | -10.06642 | -48.19217 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89aa9aa4-441e-334f-be91-b0d0b0690c70 | -15.29914 | -47.86604 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65a55e7-ed05-366b-9b9c-97c9e4fba30a | -13.62928 | -47.64362 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0746a497-6754-3c14-9152-d3fe875a8ef4 | -15.28769 | -46.4093 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 132413dd-d1dd-39df-b4e0-b0956fe68a2c | -14.61388 | -48.31634 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e0aaad0-f34f-3c04-8a12-4c2604f79bf0 | -13.36239 | -48.10557 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11759692-cf32-3000-adca-6f6fa18b9fba | -13.31543 | -47.22178 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff5cf696-7894-3292-b786-d4908f4ede24 | -17.28378 | -44.92265 | 2025-10-01 04:21:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f421dfc-b7d2-3017-bf8f-77cef3d01405 | -14.72805 | -46.8341 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1e3b8e8-12f7-3ee8-bd93-56b518635179 | -15.81756 | -41.89348 | 2025-10-01 04:21:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee30d174-bfdd-3645-ac08-cd998037df8e | -11.92332 | -47.89364 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 581ac4ef-9610-3e95-8ba1-a81449bcbc08 | -14.50243 | -48.48628 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 464cf926-4b63-3b56-8365-38fad49175c4 | -16.34039 | -43.51954 | 2025-10-01 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README54.md)
