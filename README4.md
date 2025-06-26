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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7c8bd9f-1df7-3df9-a725-4974b0e17e57 | -21.3262 | -49.06 | 2025-06-26 02:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| b8604938-ded0-3a5c-9aad-b92d5c6d956a | -9.121 | -49.4528 | 2025-06-26 02:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f2f38f5b-1f68-3c19-b42f-0266288ef179 | -10.2941 | -57.138 | 2025-06-26 02:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| bdc797ba-6b0c-310e-a2ed-f2ba0f4b94ae | -11.0644 | -55.3757 | 2025-06-26 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 317fa45e-d802-3796-a372-3397082214d9 | -6.1791 | -48.0712 | 2025-06-26 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 53e7c7cc-e89b-3153-a7cf-bd5726bdaafd | -9.4993 | -56.0988 | 2025-06-26 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f2d9ab06-9a2b-322c-86c2-b8250df51b9a | -6.1789 | -48.0929 | 2025-06-26 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| aa5f000a-2b34-3582-9057-ae60adb7323d | -7.2028 | -43.0936 | 2025-06-26 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| 03f42222-468a-33dd-ae46-96da9792cae1 | -9.1213 | -49.4313 | 2025-06-26 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| adf0ec1a-9ea9-3d1a-8054-4e6cad855f84 | -9.121 | -49.4528 | 2025-06-26 02:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 62bc99f3-ba12-36df-af48-ad4757739f21 | -9.1213 | -49.4313 | 2025-06-26 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c7c3da4d-2f13-3e97-8058-48efa7c82c4b | -6.1789 | -48.0929 | 2025-06-26 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4192b77f-2025-344e-9d28-8df4eff81768 | -11.0644 | -55.3757 | 2025-06-26 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9d052b2e-ed0c-312e-8240-8e907cef3e3f | -9.4993 | -56.0988 | 2025-06-26 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5bb66513-622f-344b-a794-104f37c0a1bc | -9.121 | -49.4528 | 2025-06-26 02:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 333e96cb-2961-3f4f-9c51-8d8554cafb23 | -7.2028 | -43.0936 | 2025-06-26 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 7413406f-1bda-3a56-b95a-c9c6141b21ba | -6.1791 | -48.0712 | 2025-06-26 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c24955ad-8805-3ec0-b7fe-3e0d9d6527db | -6.1791 | -48.0712 | 2025-06-26 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 03be928b-4c71-38c6-be7f-04d692428141 | -11.0644 | -55.3757 | 2025-06-26 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 24b825a9-1fa7-37c5-95a7-d4c002ed2d76 | -9.121 | -49.4528 | 2025-06-26 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5d0afc72-915d-3739-9b01-8124e87755c1 | -7.2028 | -43.0936 | 2025-06-26 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| bb9b2967-50d0-3305-9653-7eb9db0fba58 | -9.1213 | -49.4313 | 2025-06-26 03:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5d29a885-6492-3df7-8d18-777acbcececa | -22.14233 | -43.04875 | 2025-06-26 03:04:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7e70a53b-d7cd-3105-bb70-8454e58588ec | -22.14464 | -43.03978 | 2025-06-26 03:04:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 820458c0-fc36-3726-b75d-a78e852eb0da | -11.0644 | -55.3757 | 2025-06-26 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 57e9b079-8a99-3ed3-962c-7817a966f7b4 | -6.1789 | -48.0929 | 2025-06-26 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| abec1844-28f9-34e0-92f3-e72a6db97625 | -9.121 | -49.4528 | 2025-06-26 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 90b469ee-93b5-3137-9e51-15ebf7d24c70 | -6.1791 | -48.0712 | 2025-06-26 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 5fb34aa6-1c17-38a9-ad0b-4e58961993d2 | -7.2028 | -43.0936 | 2025-06-26 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| d61db996-f92d-3708-b37b-6534771b43b3 | -9.4993 | -56.0988 | 2025-06-26 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d2c2b01c-2df0-3528-b059-23f0b520c3fb | -9.1213 | -49.4313 | 2025-06-26 03:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a4e5609b-8a3b-3fda-945f-ab9da6a38ccf | -11.3616 | -48.7142 | 2025-06-26 03:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1d028c40-0a71-3245-8453-1a46d7a3610a | -11.0644 | -55.3757 | 2025-06-26 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a06b83d2-8414-3203-83b5-e46a56bfbc44 | -9.121 | -49.4528 | 2025-06-26 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f07d621c-df30-3634-9aa6-d4dc47fa2284 | -6.1791 | -48.0712 | 2025-06-26 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3c774c59-d334-3095-bb93-ae0ee885c20d | -9.1213 | -49.4313 | 2025-06-26 03:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 49b271d6-9b98-3a23-b2b0-6592778b80ca | -6.1789 | -48.0929 | 2025-06-26 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 9ee6d105-fca3-38d7-a0f5-3dc0d8ac2d09 | -7.2028 | -43.0936 | 2025-06-26 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 7ef9741c-7de2-3a29-a945-9dbeeca2deba | -5.72388 | -35.6124 | 2025-06-26 03:23:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef0c8185-09bf-34ea-b573-b88064d866b6 | -5.1943 | -37.69336 | 2025-06-26 03:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c8ac310-4305-32ad-887d-96e8326e5ba6 | -5.19455 | -37.69786 | 2025-06-26 03:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c1a6395-8a93-37e8-8e2a-a67be8c83223 | -4.1897 | -40.49809 | 2025-06-26 03:23:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ddf32cfd-2705-3e1b-9f05-f593c2efa376 | -4.66647 | -40.56293 | 2025-06-26 03:23:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d59fd352-2d00-3d58-9422-de44127eaa5d | -4.66718 | -40.55878 | 2025-06-26 03:23:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bd778cc1-8d9b-32a4-af00-11c87dd67882 | -4.98011 | -37.401 | 2025-06-26 03:23:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc2b158c-96b0-32e9-8827-f0c91c193a2f | -4.18383 | -40.49704 | 2025-06-26 03:23:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 401615c3-bae0-34b5-9385-fe541c6e8c2d | -5.19341 | -37.69852 | 2025-06-26 03:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e51cc7b-4b6b-31e1-86ae-3ba2630c05c1 | -8.0593 | -43.10472 | 2025-06-26 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 32e7e70f-c080-32c2-b7ee-4269e8383818 | -7.19511 | -43.09514 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 721fafe8-fa4e-3faf-ae9a-5498d5866422 | -6.95489 | -42.80809 | 2025-06-26 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 508ce5be-8847-3b32-b5d1-ef589c22d52f | -11.58187 | -44.64964 | 2025-06-26 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49c16519-2ede-3c8d-aee1-64c6e9f4390e | -11.58309 | -44.64368 | 2025-06-26 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ddc519e-d927-3a63-9423-a3d34774674b | -10.65075 | -44.49621 | 2025-06-26 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8f219d8-0b66-3991-a5ec-9dba66841ad1 | -10.65196 | -44.49022 | 2025-06-26 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ee02624-a7cb-361f-a088-b2fca536cda0 | -12.76321 | -44.41041 | 2025-06-26 03:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16ddb61d-be4b-35e4-8fb8-5022abb6a8a5 | -7.20274 | -43.09065 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| fd5846dc-fa12-3aa4-9cce-eb053d133d53 | -7.20929 | -43.09192 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 51c85595-071f-3983-85b8-45ce71d04e32 | -7.20062 | -43.10202 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f7740c6b-f03b-3bf8-8527-e1393159b13d | -11.59098 | -44.63918 | 2025-06-26 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd36de6-6088-3423-b6b5-8ff1d2c6d703 | -5.91398 | -43.45947 | 2025-06-26 03:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de900cf4-bd74-3ac0-a177-87b73bc03965 | -6.95502 | -42.80673 | 2025-06-26 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cae3863b-55b4-3abd-bb37-09501687ad2c | -12.76434 | -44.40489 | 2025-06-26 03:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d602356-dfb0-3730-a341-2efe9ee0c65d | -8.87029 | -37.7921 | 2025-06-26 03:25:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d14431c-3517-33bd-aeae-386d8c55242f | -11.63037 | -41.83838 | 2025-06-26 03:25:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f47ef180-5792-3e70-8c39-0e1a8a541c63 | -11.58976 | -44.64513 | 2025-06-26 03:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc4a320e-5997-3d2d-8122-123184e2d1cd | -7.20591 | -43.09745 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 527e22a2-9465-3c3a-8f30-1d997a603706 | -7.20378 | -43.08503 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ebbf494b-3a48-350b-b0a7-a99f132d53c3 | -11.62475 | -41.83717 | 2025-06-26 03:25:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32c31143-f76c-32b6-97d5-5b1c6da21e67 | -7.20168 | -43.09634 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 79dc2874-7854-3548-a0c8-4f4cbba9acf6 | -6.9604 | -42.81464 | 2025-06-26 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| edfea906-222a-3992-a1a9-47665befbc93 | -7.207 | -43.09181 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 966c359a-bd86-3fa9-844f-af3fe811697b | -7.20807 | -43.08624 | 2025-06-26 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8fa3bdc8-a140-3226-a20e-331221889b16 | -12.76299 | -44.40764 | 2025-06-26 03:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b454abdb-7a73-3f76-919d-f98cfbd8f7e3 | -6.96139 | -42.8092 | 2025-06-26 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d95558b-4bb1-3b58-9057-6484b268c6c0 | -6.9605 | -42.81321 | 2025-06-26 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8dc10d09-bab5-3d85-8466-6f0f56133345 | -13.62422 | -42.91691 | 2025-06-26 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bd5820f5-dfcb-3412-9faa-3e8803735412 | -20.254 | -46.73113 | 2025-06-26 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90c44e1b-3ec5-3bfb-927e-d915bff8cae0 | -17.19797 | -44.33265 | 2025-06-26 03:28:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3ac7975-f81b-32c0-bcf9-2ca51af386f6 | -18.60885 | -44.26162 | 2025-06-26 03:28:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98897782-20e6-3521-b762-bb70715b8caa | -20.25545 | -46.72504 | 2025-06-26 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2b544df-53ef-3b4a-85e4-254ebee92c65 | -17.19604 | -44.32978 | 2025-06-26 03:28:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1b1e197-1803-36c9-a429-18d82a5034ca | -18.61458 | -44.26306 | 2025-06-26 03:28:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e5f900c-7a1b-350a-8418-aa0d88875faf | -20.25242 | -46.73779 | 2025-06-26 03:28:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 460760f6-1649-3273-88fe-ae16bc26029b | -17.19896 | -44.32817 | 2025-06-26 03:28:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0837f5d-c88b-3497-843b-101cf6c307dd | -16.04367 | -43.81758 | 2025-06-26 03:28:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e35bc9da-75a9-3209-819a-d13be5b25ed1 | -9.121 | -49.4528 | 2025-06-26 03:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b316002c-b6df-3821-ae32-8f000ce36fd8 | -9.1213 | -49.4313 | 2025-06-26 03:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1aa62da5-04c5-3e96-9920-4d960d3b26ab | -6.1791 | -48.0712 | 2025-06-26 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 0df2d72a-8a32-3a00-865c-bf6089dd1abe | -6.1789 | -48.0929 | 2025-06-26 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| af17ca26-f977-3ac1-96c7-84d971df5895 | -7.2028 | -43.0936 | 2025-06-26 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 70100d87-d0df-3994-b56b-195dc2f4666e | -11.0644 | -55.3757 | 2025-06-26 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1a2343a1-e292-3a7e-8878-45559c9af4a3 | -22.14148 | -43.0368 | 2025-06-26 03:30:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3c0465ba-87a7-3ed2-8cfd-21c708724356 | -22.14422 | -43.04081 | 2025-06-26 03:30:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a537a495-33da-3eea-83d6-9e14a708dd82 | -21.18968 | -48.68816 | 2025-06-26 03:30:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bdbe92da-9618-321b-b687-9733367284e6 | -22.67551 | -42.8535 | 2025-06-26 03:30:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4d10c0cc-8b28-3508-ad44-d93b0ca0012a | -11.0644 | -55.3757 | 2025-06-26 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 493eb6d8-f5a9-358c-88cf-d0557d64ce6e | -6.1791 | -48.0712 | 2025-06-26 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6cb562e3-856c-3a52-9093-b52c5c7b1fe4 | -9.1213 | -49.4313 | 2025-06-26 03:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 448aaae3-41c0-3540-829d-5c5f629f82e5 | -9.121 | -49.4528 | 2025-06-26 03:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 8e4ac43b-3eba-3a1c-a08c-23abc39c7e72 | -9.85795 | -44.69784 | 2025-06-26 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
