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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 882878cc-1330-372c-bc9b-f5eb1e160e93 | -13.64176 | -46.46378 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f47cdf-af18-3400-ba06-ad032276f116 | -10.55305 | -44.84137 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a01003-46ca-3ef2-8832-ab323dfb29f5 | -10.85245 | -47.89115 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e43b76e5-1415-3c62-ac84-e739dbd5355b | -9.88345 | -44.881 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e7d653e-0cf4-3a97-9954-dfbc5b7c14f5 | -10.20906 | -45.95298 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14e59dc2-800a-3bba-a84e-74fec2962aec | -9.09318 | -47.81739 | 2025-10-29 04:46:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcc3ef96-9577-3c04-9307-f6e4d133806d | -10.85651 | -48.6432 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b25e5e79-6e52-3cf1-9794-bcbc2b40e684 | -10.54351 | -45.05125 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fad83ffd-b843-36b0-83e7-d530e6067a71 | -10.38843 | -47.12004 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8088df5a-e474-3f74-8c76-5453b5b2efba | -12.94241 | -46.53649 | 2025-10-29 04:46:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05042ced-2d02-36e2-b771-c656006f14b8 | -11.85187 | -47.91941 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 555f00db-7ba6-3f0f-a132-65eb05269b20 | -14.3118 | -46.5237 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4f7b969-8380-34fa-a548-2d59b4bde149 | -10.7514 | -44.75104 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b003f279-e3c6-39b1-8ee7-2f92c0c39d77 | -13.91236 | -48.47091 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f34fb604-8c99-37ae-a7e7-a586b81d15f6 | -14.55067 | -49.26364 | 2025-10-29 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03f9f368-480d-31bf-8ec9-f1abfdc2d344 | -10.76401 | -47.83395 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 759a88c7-10cb-37d4-9def-1ea467f4ddfa | -13.602 | -48.42405 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e0a1e7f-3518-32e1-b1b9-3cecaa6f727c | -11.73563 | -49.33115 | 2025-10-29 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5706337-2827-3abd-aed1-515c429fbca6 | -9.87891 | -44.88032 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e7f47d0-e0b7-3601-8367-369d1c62cc87 | -10.98391 | -47.86224 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98e323cc-5ab7-31cf-b293-6594b4c7ccfe | -10.89974 | -48.37902 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19631b0b-5a9d-3def-9f56-a59f8e630a52 | -11.03217 | -47.85022 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5d0a67a-4ff6-319a-86ce-2c49673a3916 | -13.27286 | -47.73371 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70747c25-cef9-39c2-808f-10766e532888 | -9.90641 | -44.92508 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c24ac3c9-0d30-3454-833b-d0bbb7beb716 | -13.91991 | -48.46831 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdd33de1-ef36-3966-8b30-4cc20540a61b | -13.645 | -47.03916 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b23dda9-597f-3536-b182-6193e11eca28 | -15.16642 | -47.23162 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ca3d724-120b-329e-8297-9f2a5bd0b156 | -9.62441 | -46.86543 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ca90704-1781-39a4-90e9-3b055dc3b67e | -13.66272 | -47.17764 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9514cc12-c40a-38e4-9f7b-f9fa7f5976b6 | -15.16857 | -47.21489 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf402437-e269-3b62-9450-476bd470ef72 | -12.87819 | -48.27663 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 679ad281-fbe7-3a9d-b6e8-7e27b23d3dfc | -15.3104 | -48.05558 | 2025-10-29 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5a22201-cf70-3b0a-b92d-69b2a23239ae | -13.416 | -47.38201 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29773374-7d20-3dd1-ad43-5ee6b01bd4c2 | -13.60265 | -48.41932 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50635024-69b0-35f8-aae8-2ab2895d1e8f | -13.79133 | -52.7921 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b390a11-c28b-3149-8de3-10ba7c2da08d | -13.94598 | -48.47631 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78f19842-f829-330e-b091-fc516b01dc39 | -12.83001 | -47.26789 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 226795b4-fe94-3138-877d-b81dce4c6518 | -12.70575 | -46.30587 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 750fac7a-d10a-381d-96b3-1f0760ed7441 | -13.02078 | -48.77303 | 2025-10-29 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9af8fc03-983e-3dee-a535-895d5a809c87 | -12.52258 | -49.58016 | 2025-10-29 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea03d90-b023-35fa-8454-c774c6949768 | -10.56707 | -49.83887 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0bd316b8-4f7c-3f34-a98f-bc64a4d62362 | -10.8825 | -50.0893 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10db4a3-27b2-3349-bd6a-8790ca126205 | -13.70203 | -47.67361 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 165b468a-b6e6-3eaf-8c6d-10b2c51eb6a3 | -9.18551 | -48.84421 | 2025-10-29 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f9346fd-8dee-34d9-b590-f269b83d7c02 | -11.43803 | -54.09266 | 2025-10-29 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64dd851e-a563-312c-b711-8980cecd4e12 | -12.69708 | -46.30531 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2a9a3c62-0095-34bb-89d7-484a7d75bd22 | -9.80835 | -47.60699 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4b4bc28f-e4cf-330c-aacc-bc95c6c07e0f | -10.12412 | -44.83594 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5f1b4b7-141f-3fab-bbb9-ec2d793e169a | -10.8998 | -48.373 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42227c1-eaad-3b52-81d0-c3641f6f76b4 | -12.6431 | -46.71522 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9081787a-3c3e-311e-8017-e24f324e2e2f | -13.2103 | -47.06549 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2774ab9d-459e-3efb-bf97-0fff4ec7fe94 | -13.03901 | -47.58102 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 829f82b6-c0c5-36ff-bed0-c8e22d4a9177 | -14.31349 | -48.01245 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 610f0b49-be92-328f-ac88-2ab51890b910 | -13.632 | -46.5225 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 533395c9-4f69-3ab4-91f9-1b6dfa4a2014 | -9.5062 | -46.96483 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 901aabda-1a21-3d53-88fe-39e88a307a58 | -14.48129 | -45.2602 | 2025-10-29 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba17ca36-5f14-3ba1-b19a-a8c03be83cf7 | -13.47607 | -47.45422 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8052f6c1-f811-33fd-ad14-8ff9ced71514 | -12.28936 | -47.00611 | 2025-10-29 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8d56a23-6447-3bcc-8129-8175385bfe2e | -13.64158 | -46.4972 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ecca4c4-fcdd-3c1e-88c2-02323a28a3cb | -13.93914 | -48.44154 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24aee880-7314-3911-9302-73dced0e3329 | -12.98172 | -48.39084 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f92d7026-327f-35b3-86d0-fdd2a5e3436d | -13.52548 | -47.33622 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef9bacb8-38c2-3fa4-8d09-6beb7a774203 | -10.88648 | -50.08609 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 299b5ae8-5284-389c-9721-e2301177fff7 | -11.97498 | -49.94062 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5d67ec8-a8d7-310f-8d00-071ba8954e56 | -13.53192 | -47.35061 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93e92a47-ef49-3f4c-98ab-e9ec1cd811ab | -12.46429 | -43.58471 | 2025-10-29 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03327d69-6313-3f12-82ba-8708ae1f23ec | -13.69857 | -47.6855 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e6b665c-c3ac-3808-80da-6aec2680a8e5 | -13.68315 | -47.6924 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c30f2f3-e413-3790-8140-26baa2388fae | -13.26677 | -47.72562 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 584c1b61-ff11-349b-ab98-80e37b12f40e | -12.01415 | -46.77584 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b8321905-b1bf-310c-9214-f684a25b5d11 | -14.31611 | -46.52449 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2086650-eb09-3aeb-9986-bfe8e9706c00 | -12.15779 | -47.90812 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4bbd0c3-163f-328f-b548-d99eaeee6469 | -9.33018 | -49.8215 | 2025-10-29 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2b9e921-4b3b-3b96-ba8e-764c7e1415b5 | -12.21305 | -47.90587 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d1a89a8-1c8b-310b-99cd-df5fabb850a5 | -13.64866 | -48.45076 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98796db0-a794-3f04-8a1c-fa742377f88e | -14.12866 | -44.07051 | 2025-10-29 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dea0734-b656-387e-8edb-7dad32ced07e | -15.18284 | -47.23625 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df27871e-230b-37dc-a692-ec77f584f186 | -12.96438 | -49.96529 | 2025-10-29 04:46:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5785de4-ba08-3f37-8a30-9f4da82bdc4b | -11.2787 | -45.51412 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 49d30056-3f8f-3a75-90b5-405a6cffa248 | -14.25289 | -48.10548 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe6f0fb7-e22e-338f-8308-dec6e9826b8a | -13.24057 | -47.05893 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 860703b0-8520-3427-9dad-e9ea89809892 | -10.86717 | -50.0984 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6833f499-d366-3262-b63a-ba1d471d1894 | -9.54818 | -46.92445 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83bafca0-d539-3045-8e09-fb2465bb8667 | -12.0887 | -47.25612 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d26de796-e694-3c85-80a9-70a342c4162d | -10.36789 | -47.56046 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea4b680f-e4b4-3f7f-8cfd-658a656f47ed | -14.49948 | -47.8836 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5070b76-0814-3f1d-8d19-34e703be2be7 | -9.75889 | -47.86283 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d16aef5e-069e-3405-9f6b-f0ede963c506 | -13.63841 | -46.4884 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9521da76-c2f4-3d53-8bb4-c649ab700ada | -13.94347 | -48.4664 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ddae46b-e568-364c-a4c5-78cb9574d820 | -8.72059 | -50.00965 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e90c8759-230e-3efb-987d-24c06caa6814 | -14.51846 | -48.00212 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| afd35aae-c1a3-3f68-9271-5ecbdff07ac1 | -9.90315 | -44.9151 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4040544a-c706-3d79-8b18-9a3ce710a30a | -10.6215 | -47.88498 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503745bb-1af5-3efb-80fe-2799732201a0 | -10.50406 | -47.73544 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d94f307-a8e7-36f1-98ed-7caa3b96dd19 | -13.87528 | -48.48598 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5194412c-a117-3f23-9f56-32b42fdcf9a1 | -10.8609 | -50.09361 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 377d034d-2e53-36e1-89de-3c087ecf828d | -14.2404 | -48.10932 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2d43a364-7069-3383-b68d-eaa5948288c5 | -13.34476 | -46.35275 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a00a8bca-a1ff-3eb8-91f9-36d8112932c6 | -13.17858 | -48.44553 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73b0fbb2-6012-37af-bca0-583ba7e8e83f | -13.8588 | -48.4929 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README73.md)
