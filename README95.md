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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3407db1-0f81-344a-a00f-1e9c9369424b | -19.69204 | -48.77858 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21137c90-e713-354b-b10e-befb7fb63d18 | -19.67521 | -48.79234 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 04ee7110-4ad5-3f71-affd-c10a2877b30a | -19.6745 | -48.79646 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| fe2fba85-cedc-364f-ad12-75d0da368115 | -19.67172 | -48.79161 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 63e737e6-436a-35e3-8938-baa0c8df86ba | -19.67101 | -48.79573 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 52689045-dc94-3ed0-98f6-9fa62784ffc2 | -19.66822 | -48.79089 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c1c20ff3-0fd7-35af-9247-cf921bccb697 | -20.65566 | -48.7721 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 67346d73-da08-39c9-9ef2-c37c17700eee | -20.65426 | -48.78028 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| faa113fd-5d78-3710-912b-768f189ba6f2 | -20.65219 | -48.77144 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6a61a674-5582-3573-a68b-be7c70cb19da | -20.65149 | -48.77554 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35685139-1dd5-304c-89b9-ea530737e6b5 | -20.65013 | -48.76255 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9477a443-2a92-3da3-b8b4-de0887ae5de2 | -20.64875 | -48.7497 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88f86336-41c4-3953-90e4-2bc62b092e93 | -20.64872 | -48.77077 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b82b98c-2768-3349-90cf-c70f628b7deb | -20.64802 | -48.77487 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ad5f85d-5837-3fe6-b6fd-1552d3807299 | -20.64528 | -48.74905 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fe5b50a3-7e01-3661-93d2-f521548a5bb8 | -20.64459 | -48.75309 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2ba78167-9726-3c9e-b715-0a268ac2f97c | -20.64181 | -48.7484 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3386bfc8-bee7-3089-a0df-9244dc193cdb | -20.64112 | -48.75242 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 20eab9bb-234d-3623-af19-316a031b0975 | -20.64043 | -48.75647 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 750bf8f6-096b-371e-9459-ba973273d800 | -20.63766 | -48.75177 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 086c7a19-a0a7-38f0-84ec-bbf5532b240e | -20.63696 | -48.75581 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8ad32192-d24e-3696-bd79-026335be5e47 | -20.6335 | -48.75517 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4946844e-b435-3cf8-bb2e-94aef4c3843b | -20.6328 | -48.75924 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bcf3d9c8-62d0-3f48-b06a-f349dcf82c09 | -20.63003 | -48.75452 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 329fe898-6257-31cd-8e93-baa8d9fa818c | -20.62655 | -48.75388 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 1044262c-ffd9-3f91-9562-211e0ce4aa74 | -20.62309 | -48.75324 | 2024-10-01 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3296b91c-90a2-33d1-962c-b186e6f790eb | -22.37245 | -49.33145 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 91c63565-6b5f-39fb-9057-85cf4db53134 | -22.37184 | -49.31425 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 747cc38d-d92b-33b4-b99f-2b0b651030d9 | -22.37028 | -49.34386 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 46e383d5-a47a-332c-9664-67d7247617eb | -22.36694 | -49.32175 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ce32d27a-7287-30d0-a12d-db6c3278e040 | -22.36633 | -49.30463 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 67e376a7-012f-33f4-ba35-0b5c22a27aa4 | -22.36561 | -49.30874 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6d2a140c-ab18-3f4a-9620-a94fa80e4879 | -22.36418 | -49.31696 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1cce00ec-a7e2-3911-b350-18d59343290a | -22.36069 | -49.31629 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e6e4d643-cd28-384b-b60a-ffc9a236f063 | -22.36058 | -49.33756 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3a327136-3893-32c3-a794-cd7f09d31391 | -22.37533 | -49.3149 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 520d50ab-97a1-343d-9862-651e94df4688 | -22.36837 | -49.31356 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 6869a181-2054-3f09-9ff6-72d69c19eaf8 | -22.36765 | -49.31765 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| f23546c4-c79c-37c6-906c-7548d9c7fe99 | -22.36622 | -49.32589 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| de84e100-4b94-3318-9318-4d14befe0653 | -22.36489 | -49.31285 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| eaf06bcd-6a16-31c5-b6c0-8c90a809cff1 | -22.36478 | -49.33414 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 57aad453-58a0-33bb-b1e5-391f44f0bf98 | -22.36286 | -49.30391 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 92b587fd-edf1-37ce-9fdd-a5d4c368d087 | -22.36202 | -49.32933 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| ae92c1de-b9f5-3a86-a14e-3844b5729bd3 | -22.36142 | -49.31215 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c94156ff-41b7-31e4-a713-95f424a94499 | -22.3613 | -49.33345 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| 1513ccfe-b3bc-34cc-8c41-205bc4471a31 | -21.38128 | -48.47197 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f020dfdb-d61e-3e37-8124-fd80b7e4b156 | -21.38061 | -48.47596 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f96455b5-f0e0-3974-8363-78f777488220 | -21.37721 | -48.47523 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d646f23e-3590-313f-9f46-6a07ebc2fa93 | -21.37654 | -48.47921 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10299887-d48e-3171-b6b7-6d59b3aed359 | -21.37588 | -48.48317 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce5c813-877b-3443-829c-44b3d23e084a | -21.37521 | -48.48713 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6eb8908-9f72-3c3b-8f13-227860f7edb1 | -21.37114 | -48.49038 | 2024-10-01 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce9d56ea-19b7-31a2-93bc-838981b6506e | -21.31289 | -49.23788 | 2024-10-01 04:17:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3f649f26-5fb2-3ff6-a3b3-b51dac21540d | -21.30938 | -49.23717 | 2024-10-01 04:17:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 550c4c2a-db7e-3caf-96c9-d88bc149a87b | -21.30588 | -49.23646 | 2024-10-01 04:17:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7b240e42-db40-3e1a-ac29-21c1d3e389cb | -21.3031 | -49.2316 | 2024-10-01 04:17:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2fcc9e87-ecaf-3bd8-aa44-3302f602e77e | -21.09439 | -49.1365 | 2024-10-01 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a649f088-0724-3e20-b0e3-72cf16c79a7d | -22.37881 | -49.31556 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a898a5cd-4e8d-3850-aca6-d7fc889b42a9 | -22.37604 | -49.31081 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 565fe799-b17e-3fb7-8d86-1b5c41a93b62 | -22.37519 | -49.33633 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 389c1dc3-07d3-3acd-ab04-fde4a58c908b | -22.37461 | -49.31899 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc4cd5b9-1fc7-3d77-9391-69061064bb19 | -22.37328 | -49.30603 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 2710f3c8-98da-3fe6-905e-36ed0db7ecba | -22.37172 | -49.33561 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| da2932ee-bb29-342c-9a94-42e14355def2 | -22.36908 | -49.30946 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 0f037704-027c-3cac-a5ba-90a1a75859a1 | -22.36825 | -49.33487 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| c46fba57-48df-385d-b0d8-22e30eb50b76 | -22.36753 | -49.33901 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| f5083e93-48d5-3b8b-9563-6fc8fd8e2c32 | -22.3655 | -49.33002 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 1aa85c66-0ea0-374f-a535-565deb083242 | -22.36346 | -49.32108 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a221c241-99f6-36cc-bae7-1424468997ee | -22.36274 | -49.32521 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| e8e3c3b4-9670-3faf-bffd-20a22d2ea046 | -22.36214 | -49.30803 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c658a70d-d861-37ae-9ded-70b75b26551a | -22.37447 | -49.34047 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| bc8abc20-15f8-3ffb-93de-0c52151db841 | -22.37256 | -49.31015 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 5fae521d-3443-3062-8e0d-3329ad11793e | -22.37114 | -49.31833 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| e0a0ca75-0919-3d4e-89b4-5ca244c8468e | -22.371 | -49.33974 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| c55dffb9-a26a-3a71-be07-bdf37648423c | -22.3698 | -49.30535 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 67a85a39-e898-39f7-8e8f-bd15b9e5ffee | -22.36897 | -49.33073 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| e52a1df0-a8d3-3d01-be0f-d116deca7cd1 | -22.36705 | -49.30051 | 2024-10-01 04:17:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5e5609f2-c2a8-3e10-9c71-91b2c6864c3d | -22.36681 | -49.34315 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 12cd723d-946a-3355-aa29-3db64f79086e | -22.36406 | -49.33827 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| ea88c1fb-4490-3ab4-b3c8-ed0b99344f88 | -22.35997 | -49.32043 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b1c13a12-065d-3801-8bf2-a360be0d20b0 | -22.35925 | -49.32455 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| bcfc8ec0-f3b7-3a47-a53a-d37151b9f0a6 | -22.35853 | -49.32867 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| d7504a78-32c9-3df2-b3c8-b6e69c61f90a | -22.35781 | -49.33279 | 2024-10-01 04:17:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| ed893851-e1ee-3a0f-a336-971c0e9aaff5 | -22.21405 | -49.96857 | 2024-10-01 04:17:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ee5cbf7-0555-3bad-bba2-bb8a2a453500 | -22.5393 | -48.81405 | 2024-10-01 04:17:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e4950bd-d0be-33e4-8ac1-3ffdeed42672 | -22.99988 | -49.60952 | 2024-10-01 04:17:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9900259-e2a4-3616-aac9-8f215d1ed183 | -22.99639 | -49.60882 | 2024-10-01 04:17:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c193baa-b021-30ab-b5dc-f908dcd1e8e5 | -17.86504 | -49.91013 | 2024-10-01 04:17:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e453f464-55d9-335d-b3cd-78b46e483e6d | -20.17278 | -50.00633 | 2024-10-01 04:17:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| be602be8-fb0e-3b23-9027-e3e1fc1b15dd | -20.17194 | -50.01096 | 2024-10-01 04:17:00 | NOAA-20 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2f947a15-01c0-34b7-9834-ff2b8454d2a2 | -21.5577 | -50.76779 | 2024-10-01 04:17:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 456a90da-ad4e-3036-aabe-0a69f6e86899 | -21.55395 | -50.76698 | 2024-10-01 04:17:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 17ae725d-81f5-340e-b5c6-11bc450d3704 | -21.54362 | -50.75967 | 2024-10-01 04:17:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f374814f-5267-38f0-a38c-85ceffc6adc2 | -21.54303 | -50.76204 | 2024-10-01 04:17:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d74602c6-7252-3eb8-9b1c-3ccdb5648105 | -21.5427 | -50.7646 | 2024-10-01 04:17:00 | NOAA-20 | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 636a9d28-30e0-3edd-b2de-c1afe5e1c851 | -23.56899 | -51.42727 | 2024-10-01 04:17:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2bda3658-352a-33e1-962c-f01968d06fb7 | -22.78369 | -50.61172 | 2024-10-01 04:17:00 | NOAA-20 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| be2b7be4-3c0b-3205-ac67-3e1050463b8e | -19.3067 | -52.13592 | 2024-10-01 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcde52ae-983f-31f6-ad1b-523ca29c2e84 | -19.3017 | -52.13912 | 2024-10-01 04:17:00 | NOAA-20 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9dfad73-65b1-378c-b458-cb14b82a2aec | -20.08293 | -51.32689 | 2024-10-01 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README96.md)
