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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50fc800c-265a-30f7-8ded-53a1828895df | -10.70141 | -49.51832 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 802fe78c-6e91-36cc-8d67-0da72c0f390c | -10.94534 | -55.31699 | 2025-06-11 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55e66ca3-4cf1-3f4f-9780-508176de4da1 | -13.56755 | -44.27502 | 2025-06-11 04:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1981abaa-b948-3979-b82f-9504cd9bc698 | -10.24894 | -46.48145 | 2025-06-11 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec22d045-1a8e-3e81-8627-b525f5310b22 | -10.18472 | -47.31805 | 2025-06-11 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96777b8a-2c90-3649-9897-5283890700c6 | -10.87222 | -54.32422 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 586c5507-e848-3306-a7dc-12a02eefc52f | -11.13704 | -53.94611 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a190d35-a41a-3878-99b4-07d92ba08914 | -9.77669 | -57.42633 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 088751e7-0770-378b-9d78-8c80d02eeb0f | -10.87824 | -54.74441 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2daf2920-0b07-37b6-a2b1-36a4c952b171 | -9.60786 | -49.01513 | 2025-06-11 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00201d86-c0a4-364d-8da0-d8ba9dbaa993 | -9.85909 | -57.64469 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07082154-bb11-32aa-bf8e-4297966ef4b6 | -12.25931 | -57.61245 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 569bf229-bf07-3a78-82d1-3ef34683b372 | -10.0734 | -52.7472 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 375a854c-29f8-3a54-bedb-1a86cf2f3363 | -12.1026 | -49.48109 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42d7b5ec-5b84-3f70-97f5-e04357d5bb34 | -12.20393 | -49.62481 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ac9039a-ad05-37a9-960b-8059ddefd402 | -10.89961 | -42.24184 | 2025-06-11 04:49:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a9526be-942e-3569-bbb6-e825883045c2 | -10.65687 | -49.43016 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0c4460bc-0a53-35bf-aa0d-96c4651d4d47 | -8.91487 | -48.90497 | 2025-06-11 04:49:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c318cb0e-7cc1-39fb-b8f1-c51c7d609b1a | -11.39905 | -47.63685 | 2025-06-11 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a55119a1-c845-3285-8ebc-e01f072e1da0 | -10.24012 | -52.23138 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7974ad59-a1e3-31d0-8c23-7e85938e77b6 | -11.56989 | -47.43431 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02744c1e-ee95-3bbf-8edc-ed6fdf40ad80 | -11.88439 | -56.41525 | 2025-06-11 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e20ad5-21c6-3600-bd64-e92f9e9aa094 | -11.77224 | -54.38078 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4292f851-2ebf-3efe-ae3c-3353112ba63b | -9.8899 | -47.8099 | 2025-06-11 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d09b4b2-3edf-3ad3-94f9-101cb1dbcb64 | -9.10573 | -46.05921 | 2025-06-11 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30e0abe5-c585-376b-9b8d-006fecf170e9 | -14.2448 | -45.4994 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ffa41da-1252-308e-818b-bcee043b2751 | -14.53329 | -46.03853 | 2025-06-11 04:49:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 71b27b5d-dfa4-3401-94ef-4ded04d8f5cb | -11.81586 | -46.14058 | 2025-06-11 04:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03477e77-d7c0-34ba-a505-af0c3f7dd5f5 | -13.56793 | -44.27203 | 2025-06-11 04:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fdb75ef-2b70-3dad-b4f0-ef452e2af03a | -12.06464 | -47.31915 | 2025-06-11 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9fa9fa2-4409-3f80-89ea-43466937fd18 | -10.18736 | -49.58805 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45bfe60a-76a7-32bb-8fc3-f328424f4a80 | -9.3229 | -50.3269 | 2025-06-11 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c8aaaf-dcfd-3a6c-bb23-3506bdab085e | -10.18627 | -47.31667 | 2025-06-11 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf1c455c-dac2-3ce7-bfed-8d00f65b16f5 | -12.77912 | -48.72923 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 288b1425-52a5-3144-b9e1-1477c64279f1 | -12.34568 | -57.42837 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45458c22-1171-3497-b6d3-e1d6c3bd2255 | -12.06818 | -47.32335 | 2025-06-11 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 042d86e9-d874-326a-b1cf-af7dde547161 | -11.76942 | -54.37636 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ce34234-82bd-3ddc-899c-a0db941e1f8e | -9.86332 | -57.64546 | 2025-06-11 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f3bd618-dad5-3900-82be-811c029e7975 | -12.26402 | -57.60953 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ab04354-04a5-3e80-84ea-42ef1e4c803f | -11.58264 | -51.34543 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d97830d0-0d51-3384-8772-dda08b43d829 | -10.85153 | -53.79276 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2a368ef-248e-321d-adee-c841b3e7e962 | -12.21105 | -49.62587 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55bffc49-3e7d-3965-b382-ee24f6ac07e9 | -13.52141 | -47.86297 | 2025-06-11 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 175937fb-a4cd-3512-8e83-24d32b19973d | -12.25996 | -57.6088 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cd47783-b92d-3f2e-86a1-fa047467af2c | -11.05259 | -55.03916 | 2025-06-11 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0e0398-588e-39e7-9251-92cf4174b5c1 | -10.19493 | -49.58523 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f62429c2-da42-3505-899b-382eb0b72500 | -10.63861 | -49.43141 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20cd6736-2c75-3adf-b415-8ab1bf4238da | -12.5195 | -57.22838 | 2025-06-11 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 831f4a55-8772-3a90-8ba8-9693fe8f7683 | -8.69549 | -49.84943 | 2025-06-11 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bbdbf9a-58ca-3f4f-9d85-39c7ca4a7c94 | -11.63083 | -47.68859 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e3b7930-e8ce-3bc5-9d24-e65c97458e5b | -11.77757 | -54.36993 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d654425c-b6e5-3e2e-bf0d-d4806839bb47 | -9.38221 | -48.41297 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee153475-2f47-36d3-b56c-f7532f4c7013 | -11.58654 | -51.34238 | 2025-06-11 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25ce827d-255f-3945-a1ec-70b051533434 | -10.50712 | -53.63418 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f94ed28-d835-31a7-ad11-9f38a20bbb08 | -9.09166 | -49.64759 | 2025-06-11 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8161e10-094e-3288-b309-9f4cbbb56218 | -12.78278 | -48.73182 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6742b4e-ec97-3286-8806-0282746f2d78 | -10.661 | -49.42666 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 341c8f6d-7f50-3b99-8df2-e7709423f605 | -11.77004 | -54.37254 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067cca3e-5486-3cab-b18b-088abcb66c70 | -10.87757 | -54.74842 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb5cfc06-09c9-3c3e-bc8b-e9745eb53d3f | -11.88059 | -56.41459 | 2025-06-11 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f53086f7-f121-388f-b320-566f44abf238 | -10.50585 | -53.57712 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86c433e3-9279-37d3-8cfb-032482561135 | -8.71762 | -47.85065 | 2025-06-11 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df9dca88-fdca-3459-bdff-0a8478452589 | -11.37662 | -56.55924 | 2025-06-11 04:49:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8783da83-865d-3581-b681-2f1ef2277de6 | -14.25554 | -45.49038 | 2025-06-11 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be9331df-34d6-3b91-88dc-3f898391bd23 | -11.77977 | -54.37817 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da576bfa-1347-3f61-9aa9-caaf78308faa | -11.49611 | -48.58936 | 2025-06-11 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8051e504-2a4f-3aea-a35d-0e21864546a9 | -13.51741 | -47.86246 | 2025-06-11 04:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fa42040-e49a-3274-a667-e8dfac44714c | -12.77966 | -48.72675 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a80723e4-f9c9-3fcf-ab92-b4528711e8b0 | -10.64214 | -49.43197 | 2025-06-11 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eb94b8e-1842-3758-a792-a1d0c9b4f0f6 | -14.50125 | -43.80618 | 2025-06-11 04:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd298077-8d87-398c-a2f7-81c9ff740539 | -10.51376 | -53.63461 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 954fbe12-3bd6-381c-b448-6eea9c24609e | -11.1395 | -53.93112 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca236f79-5a54-3ae2-9501-0bfc23016ad7 | -10.87689 | -54.75245 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c4430b0-d48d-39e5-b011-6e0e4bdebb78 | -10.88178 | -54.745 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8185776b-c2f0-3001-a00a-7ced1e0eee3e | -11.63023 | -47.68579 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6460b070-9860-32ab-a83a-e51fc91a01b4 | -11.76659 | -54.37195 | 2025-06-11 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b60ea51b-d950-31c9-8e9f-f519510cd199 | -10.51036 | -53.63404 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c920f4e-e525-3072-927c-b42db98f3bbe | -10.87286 | -54.32037 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c5e9247-1a9a-3beb-ad5d-63e3062370c5 | -9.34991 | -50.2639 | 2025-06-11 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4bf060-d291-3ad5-bf45-4f83bc2f5e80 | -11.56822 | -47.43232 | 2025-06-11 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a63ac1ab-cb0a-3343-9904-1e502a9a6c1f | -8.42023 | -48.30653 | 2025-06-11 04:49:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70aafa8e-5c75-3df7-8aa5-152446a3b164 | -12.78341 | -48.72729 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc50f172-3a16-3a74-a38d-b03322dc1a0a | -10.38019 | -49.93163 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a858b36-c839-3cfb-9158-7673f03a4efd | -13.31261 | -47.13827 | 2025-06-11 04:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b0358c0-00d0-3cb3-9757-e7175cf3c651 | -10.69849 | -49.51381 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3676579-a703-356c-9532-0b0ae597b40c | -11.74195 | -46.82634 | 2025-06-11 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41cdcb65-5754-3946-9074-5d93870eb63a | -12.2133 | -49.62484 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bf46636-694d-3140-8a67-6c3caeb3b565 | -12.83626 | -47.38414 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3877a9d1-452c-3c59-b013-b87499bd4979 | -10.70201 | -49.51436 | 2025-06-11 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0a5f423b-0a0c-39a3-bc8b-111067768484 | -12.2683 | -47.00367 | 2025-06-11 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50403640-5e43-3098-a9df-120022375940 | -9.85294 | -47.87585 | 2025-06-11 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d186bd32-3f6f-3416-a757-8e02a654ac19 | -9.23868 | -63.28479 | 2025-06-11 04:49:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21385319-1ca0-3a3c-a506-48c18e823f1f | -12.19985 | -54.26395 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75282f08-ec49-38c4-9eea-58f77bf9471e | -10.84593 | -53.78417 | 2025-06-11 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7692ae5-b121-38d2-a177-a3ad9569deaa | -11.62629 | -41.83542 | 2025-06-11 04:49:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 326564d9-0d76-3a5f-abf8-feb93b334ecb | -12.83982 | -47.38836 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58be859-7762-383f-a6be-880733fb05cf | -11.04902 | -55.03851 | 2025-06-11 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc3fdfe0-c2d5-35e1-a5a7-1a2b38e753e6 | -10.50757 | -53.62978 | 2025-06-11 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c764064-3fc9-384c-a203-62e275c0cc73 | -8.2843 | -47.44619 | 2025-06-11 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9c2d106-1570-3589-8590-fc385ed71640 | -12.0406 | -54.68247 | 2025-06-11 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
