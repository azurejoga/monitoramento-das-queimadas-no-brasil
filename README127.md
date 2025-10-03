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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98437539-e0b7-3175-adc0-33fd4647e948 | -14.73532 | -48.12654 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13e10bd5-2d36-3775-9f6c-7b6767940594 | -13.29456 | -47.84 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 860b1512-3199-33b7-84aa-8ca12408e412 | -12.9121 | -46.89187 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 613a7e2d-cba5-37a8-8a2a-3bfaf3e56621 | -19.72037 | -45.90819 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ac62f0-4ab0-3557-8168-b6f708bd3353 | -14.98004 | -49.97084 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 648d92c4-e201-3024-8d79-0ddec8fc785a | -17.63069 | -44.44837 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3e30718-8271-3171-a14f-b1f7b5de1d54 | -17.96359 | -44.39508 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a612d637-45cb-3799-a7ae-5962353a3f98 | -15.21221 | -47.18881 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 002f6ec2-97eb-39f2-a8f5-9e6fb8e087d2 | -14.7312 | -48.09962 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2844be97-1d75-35f6-981f-3b5b91a25396 | -14.89829 | -46.84087 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70346881-f9fb-3cb2-a278-ea6d24df9203 | -13.96495 | -48.12082 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02a9daf0-b0f1-38ed-a5b4-050ad05240f9 | -13.13922 | -47.89825 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d319b52d-0670-369c-bcab-82489a14098a | -12.86309 | -47.00715 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02f6e862-4d4c-3ff1-858f-a800c4609a7a | -14.67266 | -48.09756 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd39c451-a7b2-3e9b-8fe9-2b973f7786ec | -14.57935 | -52.4702 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b4b45ac-b098-3267-b029-fe14c94a10f3 | -14.23275 | -46.10703 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2989834d-1a7f-38a0-b4ae-55e1166f2542 | -12.63832 | -46.96594 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e74990fe-9dcd-3bb5-a20d-9b87301fc25c | -15.21282 | -47.18454 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9e7a219-4cf0-3738-bad6-8878600e3613 | -12.64338 | -46.88357 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87075395-2927-35df-9d9c-e14be39e2d56 | -13.94532 | -48.15903 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c29d31d-7bf6-3cdb-bb1b-88a111030734 | -14.60262 | -48.24146 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b80dbd36-7a73-333e-bb48-bafc10f6ee38 | -14.28865 | -45.9191 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45aa9c51-a3ad-3da6-a85b-bd0140803933 | -19.60121 | -44.62896 | 2025-10-03 04:34:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85cbcfdc-c7a3-3999-8205-ea6f200c9f84 | -18.22722 | -53.36417 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d02996ac-be96-39ea-8465-9158f54464b5 | -13.22891 | -46.43497 | 2025-10-03 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef372dce-1f1c-39ce-bb5b-2ea23c90acda | -14.91158 | -48.35145 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6827c34-0a99-339f-a817-90dddd603588 | -14.35873 | -43.84004 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed40cb18-8b5d-32b0-9cf6-584ee4674307 | -13.59053 | -48.19188 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97a2d38f-3b44-3328-8c5f-601b8dabc631 | -13.34152 | -48.08595 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 629e416d-2357-3ce2-ad0e-f7c2f31a7596 | -15.08813 | -49.56498 | 2025-10-03 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0192f85d-a1f1-36b8-8659-55bd97118d08 | -15.94576 | -46.22587 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 440bc037-d7e7-3c83-b2aa-875853a3c76f | -14.62391 | -48.23751 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 736fe4a1-341c-3710-b29f-40353e51aa07 | -14.37702 | -48.47998 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cc02e50b-22b1-3c68-b05c-13648e1a3ace | -12.62323 | -46.98065 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1f63fd57-ee77-3283-9ccc-f436e07f1e36 | -20.37121 | -42.20365 | 2025-10-03 04:34:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 266d3ebf-b34d-3c2b-94bd-760876b7fcf6 | -15.37659 | -48.60061 | 2025-10-03 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f973a8-f4e5-37e2-b729-3e8187349d27 | -13.51539 | -47.25465 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baac8594-aa1a-38ee-a91b-945412487eff | -12.94081 | -48.44693 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0d4d88-3dbb-3298-a284-5c2cd30133c3 | -14.00817 | -44.92469 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23266178-9173-3bc4-855d-a21dfd71ac86 | -13.76864 | -48.04008 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cdcadca-823a-3203-a7bc-1b0c43e80999 | -13.86411 | -47.93444 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32fcb5d9-cc8a-33af-af1b-7d6b443af0fa | -13.13975 | -50.02636 | 2025-10-03 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c79321e6-2a96-381b-9e16-a8539ed4105b | -12.19722 | -47.80774 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75e2891-23e9-35cf-a319-d3b63eae569b | -13.3371 | -48.11505 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dc21553-8480-38bb-803d-31a0317a682d | -14.20238 | -46.05843 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 79b8312e-240e-33ce-8bad-047c3b063878 | -12.90398 | -46.89871 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8f26d7d-b0c7-376f-9f6d-8853d3589754 | -12.71028 | -48.57475 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1689a0fe-6e6b-3894-a3ae-372c40fa273a | -12.75636 | -44.90142 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caa3a8d6-2d5b-3136-aaf9-a3312227016d | -13.75759 | -48.08013 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73550a57-2ec1-3ce6-bf53-95963b65db13 | -14.67597 | -48.0756 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b629f2d-b72b-38a1-abce-cea116fb2128 | -13.16443 | -47.37994 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a42e866-bf1e-354e-ad95-15d6564f32bc | -15.31107 | -46.38901 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1ea5986-211b-3197-bbc4-70394e00d01e | -14.46852 | -48.41183 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97666336-a89d-32cb-adce-e8b603b8863f | -13.74018 | -47.99089 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cbb07b7-f435-3b36-8abc-cb6dd3555cda | -15.34179 | -47.06632 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40b503b4-2cfe-39ea-a834-2d3a7026cedf | -13.44918 | -47.25579 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 191a1c3c-da79-3ce3-bb46-d98e8b52f9b7 | -13.4513 | -47.25922 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83659772-a04c-3ebc-9366-749cf97e9594 | -13.15316 | -47.82858 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbfa6424-cb97-36f5-9f29-ff9ca243a930 | -14.80672 | -51.41759 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d4db28d-b3c4-3899-bb04-c4bea7a1a421 | -14.74883 | -48.1287 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d69fe70d-7d2c-3bc0-b172-8ddd7880d68c | -12.62267 | -46.98439 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 19b1ad9a-b292-3a07-b686-b6027043f45b | -12.648 | -46.87623 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4afb2c51-2976-362a-80dd-d5d68819e09f | -13.20487 | -47.87468 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 077776f4-77f7-30ee-8eca-ef14c9165d3c | -14.91718 | -48.30307 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f606fbab-2d74-34b6-a751-7757769adb27 | -14.87816 | -46.8545 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50e935bf-626b-3fa1-b37a-2905ea6e362b | -15.22038 | -48.73261 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3cd1fa8-945f-3b97-9720-0d3ca15b793d | -13.79944 | -47.57683 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fe23b374-8794-3864-b4fa-d182baed134f | -12.90852 | -46.91592 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e13a22-ce36-3bd3-b07a-0b9caf1b1055 | -12.76336 | -44.90729 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60517597-d4c6-3b71-b577-77d403be1229 | -14.90811 | -46.97146 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a0ae298-57f3-3142-9e5b-0ee4881355a0 | -19.23325 | -43.71641 | 2025-10-03 04:34:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 970f189f-c4d0-3ad6-bf89-ec1ad50c286a | -17.51548 | -43.4857 | 2025-10-03 04:34:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b457bcba-2ed6-3ce4-88ae-c93c9838b74b | -19.14292 | -41.49781 | 2025-10-03 04:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| de81a6ed-b920-37d9-95ba-885aa9d3fe6a | -15.32007 | -46.29834 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10b8bd32-eaa9-39c8-808f-f67bf7cc9277 | -19.84723 | -46.16095 | 2025-10-03 04:34:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40c0b28-3714-3e80-a7c4-accfd4c9d392 | -14.01073 | -44.96827 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1db4536-a1a6-3d3e-ab9d-60e78eaff2ca | -14.64581 | -48.25234 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ca400ba-51db-3575-95d0-8ad72c14b60f | -15.22986 | -48.71548 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb0c0917-9970-37e8-b492-5c12c04e9a3b | -12.90051 | -46.89819 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11e493a-03d8-39d8-a069-ca97f8d1a728 | -12.60314 | -46.99678 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b24734c-3625-3ed0-b2a0-2cef1287119b | -14.2161 | -44.95677 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 442bd84c-1e04-3901-9368-a16f17cdb79e | -19.46896 | -43.6491 | 2025-10-03 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0dfb64aa-a930-3f0c-b875-512d70a16b11 | -12.6343 | -46.96925 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| beb5c886-e5ec-3bc1-8adc-820941901ad1 | -16.40356 | -52.15822 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4c3d7ca-e3a4-363a-8390-7d8667df6181 | -15.24143 | -50.12082 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a716e9-86a3-3882-b046-1a6790946430 | -19.90216 | -44.51202 | 2025-10-03 04:34:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ac25970-664d-3b42-b4ae-41bee94f4cdd | -14.73077 | -48.11061 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 76026910-6dbf-3a2f-9bab-22b692147253 | -14.21029 | -46.05533 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 91d960c5-7b54-3094-a80d-8993bf2bbb26 | -12.95502 | -47.16613 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb86b775-a543-389a-9a27-0c87952a8845 | -14.93691 | -46.89676 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 980ce58a-e195-38cc-88bd-43d4d920f213 | -15.55369 | -49.2783 | 2025-10-03 04:34:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bfb908d-2d38-33df-9a8d-048a1c858166 | -18.16028 | -53.35032 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6421e7b-c688-36f1-b2d9-6ca457226d29 | -18.21164 | -53.36997 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f93393c1-4398-3d38-b260-ed175a6109ee | -16.77771 | -50.11388 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4db68987-1a14-344c-9f6d-23a1c78ac418 | -14.91717 | -48.33717 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73a9a8e0-6101-395a-9123-7ee1ca0e8756 | -13.57412 | -47.58621 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d8e23cd-a132-378b-ad9d-c51e97add7cf | -13.19468 | -47.82819 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fe30299-6b2b-3036-8b80-20f5ed1686e7 | -14.90591 | -48.30903 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c180e81-c05c-3632-8a71-c13664c78200 | -13.57344 | -47.28584 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d720623-17c8-3efa-a2bd-c3d3f299f3f3 | -13.763 | -51.19113 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README128.md)
