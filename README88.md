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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b38cb8e-cdad-363c-bc96-c916aa818015 | -7.8033 | -44.8651 | 2026-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 4fba50f2-4413-3c34-80f7-3b20a0da98ae | -8.8644 | -45.8919 | 2026-09-17 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e8c2a8b5-af3b-3a93-9ae2-176b10a696f4 | -12.4333 | -48.4897 | 2026-09-17 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 592000fa-833b-3685-9d75-c741df99fbde | -9.8694 | -48.3814 | 2026-09-17 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d437f8ef-5a1f-341c-bd5e-2ac2740be454 | -12.3085 | -47.9539 | 2026-09-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4a61f044-759d-309d-b881-4a8238dec1dd | -8.8459 | -45.8713 | 2026-09-17 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| fa2849d8-b631-303b-a09c-4948047969a1 | -13.6531 | -45.97 | 2026-09-17 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a8f4bb9e-3380-30e3-8532-a4816d9e5ab1 | -6.9896 | -43.6514 | 2026-09-17 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 937df005-ba42-3369-83de-feb303e45fe2 | -7.3669 | -38.9584 | 2026-09-17 13:00:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 113.2 |
| ed487af9-240f-32f8-a2b6-76f70dbf8e9e | -7.0084 | -43.6497 | 2026-09-17 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 3e7a4ad3-8c99-39bf-8988-69f6dac2b36c | -7.0164 | -44.6413 | 2026-09-17 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| b670c76a-181c-3805-a191-85ce24e0466d | -7.6402 | -44.3303 | 2026-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 7ea16d93-31d4-3ee5-89a3-1a1fd25c3116 | -8.481 | -44.9102 | 2026-09-17 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d0e0cfb0-342f-3735-ad35-b4244ce1dca6 | -7.841 | -44.8614 | 2026-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1b27f695-36be-326f-9960-6d958413ef30 | -7.3853 | -39.0068 | 2026-09-17 13:00:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 104.8 |
| a456e205-093d-38c9-92e4-480491d20e4d | -7.0349 | -44.6625 | 2026-09-17 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f7458e5d-7fd3-3943-a515-b185eacaf786 | -11.3463 | -47.2585 | 2026-09-17 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e4d61ada-e7fc-3fee-b63e-a771a6be3734 | -11.3437 | -44.0141 | 2026-09-17 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9a14764a-0de1-31e6-9dff-1dd0279f27b4 | -12.6635 | -50.7835 | 2026-09-17 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 980596e4-2e88-36e0-9114-aa8194a72c86 | -11.8069 | -58.1759 | 2026-09-17 13:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 4d1ab5b9-2699-3530-a310-0ddd2f34636d | -10.8118 | -46.1594 | 2026-09-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 164c4635-bbb7-3be2-8873-850df23a3277 | -7.8221 | -44.8632 | 2026-09-17 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.9 |
| f3feb751-a569-3c98-969e-dc91e6b43975 | -13.6143 | -46.9561 | 2026-09-17 13:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6814d250-e705-3697-87b7-85caffef28a9 | -8.475 | -46.8943 | 2026-09-17 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 390b1d2b-e68d-3faa-b468-2c557debd201 | -12.6816 | -50.8455 | 2026-09-17 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 35b7e559-6f34-3909-aad7-ea64e1417bc0 | -7.0084 | -43.6497 | 2026-09-17 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 8be0be75-903b-3fe1-bc36-3dee2e774f1a | -9.8697 | -48.3595 | 2026-09-17 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1f496dc6-9e63-3bf4-9178-fce1d0313baa | -7.0349 | -44.6625 | 2026-09-17 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5b632e83-9974-3f1e-9642-14676f05719b | -9.8694 | -48.3814 | 2026-09-17 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 6b9aab1c-d59a-3ed8-9e0b-51d0d99ad8fd | -15.5001 | -53.8552 | 2026-09-17 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 917a0f76-831a-3227-8bbc-cc48cc6a194e | -3.2212 | -53.9422 | 2026-09-17 13:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 183.9 |
| addb76d2-432e-3aee-be8f-7cdf0506e1e7 | -14.8183 | -59.5532 | 2026-09-17 13:10:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2f91c70c-a27f-380a-a5e4-caa20bfad9b6 | -12.7894 | -51.2807 | 2026-09-17 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 04d3ea69-4dff-3940-bc56-b39142f30b14 | -12.3387 | -50.8014 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1a62ce38-5338-3a93-acce-d6159dfaebbe | -15.5004 | -53.8342 | 2026-09-17 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d2d63439-9d32-3084-a573-8fbca58df12e | -12.3568 | -50.8634 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 6f6be6d3-b95e-347d-951e-63eac847ba39 | -7.3853 | -39.0068 | 2026-09-17 13:10:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 128.4 |
| e3e85418-9bcc-3659-8b2d-0922fb4546f0 | -15.5012 | -53.7921 | 2026-09-17 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2a8943e4-3515-38da-b84a-4e54cb832e14 | -10.8919 | -54.0062 | 2026-09-17 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a19cf3a9-ebf3-3b93-867e-fcd3acf51af7 | -12.6635 | -50.7835 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 76902798-26bf-3ba9-99b7-b99880c909aa | -12.3964 | -50.7731 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 09b8e944-dcae-3b2d-8c25-4302a724eab5 | -7.0617 | -47.5046 | 2026-09-17 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 421d2c70-49ba-3269-acb2-7bb15e7b5013 | -12.4343 | -50.79 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| afc47f79-61fa-35af-b119-532b211b9784 | -10.9107 | -54.0045 | 2026-09-17 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 9a3d8d87-2628-3eca-8255-411b1485442f | -9.8884 | -48.3794 | 2026-09-17 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 52e4dd97-1f0d-34e5-b7d9-f214ce7d589b | -12.3085 | -47.9539 | 2026-09-17 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 479e83e1-8075-3dad-bea9-353650ec3ca5 | -11.3625 | -44.0347 | 2026-09-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0047e55a-666d-363a-aa57-9410f9a8c5fa | -9.7497 | -46.1089 | 2026-09-17 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 656e5447-9054-3e7a-b361-f0bf3fb77fff | -12.4155 | -50.7708 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7ec19ab3-5a46-3452-8b85-4de503432dd1 | -10.623 | -46.0704 | 2026-09-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8a9a389a-1bc6-371c-b33a-832802f690a9 | -7.3663 | -39.0091 | 2026-09-17 13:10:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 213.4 |
| a36292b8-8150-3352-b6b6-38813bfb31d9 | -10.8308 | -46.1569 | 2026-09-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 02de71f1-a4b8-3deb-a2d4-9902ad32669f | -15.4626 | -53.7761 | 2026-09-17 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 2972808a-72f7-33e2-bafc-24334cd4e34d | -7.5664 | -42.6323 | 2026-09-17 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| af78b12b-63b9-3673-a7dc-123860dc0f3f | -8.481 | -44.9102 | 2026-09-17 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 3329980d-efe2-3cb3-babf-d92cb9228abe | -12.5094 | -50.8664 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 229.2 |
| fb43dda0-3c17-3b46-9de1-39c3e2d56cd4 | -14.1932 | -45.1606 | 2026-09-17 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 53537202-a88d-3e4a-85e4-fdba5d448aa9 | -10.8757 | -50.8376 | 2026-09-17 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 61a1a097-bc2e-3490-a753-866a8e1b1db1 | -9.8319 | -48.3636 | 2026-09-17 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 00cb3e55-5685-31d1-a5f1-aaf3237537d1 | -6.9896 | -43.6514 | 2026-09-17 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0e2eb3a9-90ad-3f38-acf3-6c9d0002da0d | -7.0804 | -47.5031 | 2026-09-17 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 48650643-6d1e-3d74-846d-9c3ebd5b183a | -9.9143 | -46.5172 | 2026-09-17 13:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 265.0 |
| 83bbcd89-f2df-3666-b0b4-e4b79c4bbc74 | -7.6402 | -44.3303 | 2026-09-17 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 7ed702a5-c965-387f-b1dc-c5cce0d62ce5 | -8.8647 | -45.8693 | 2026-09-17 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a5cd3add-c7d7-31cb-bf26-81b0b5d15850 | -7.6414 | -45.8556 | 2026-09-17 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 81440568-f357-3984-8738-847afe1adade | -12.5097 | -50.845 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 0f662c4a-3a29-30ef-98bc-47fd03c07c86 | -12.7051 | -48.276 | 2026-09-17 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b8ef78ac-ecc5-3368-a2cb-e776d566cdbb | -10.8118 | -46.1594 | 2026-09-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 3dd1c53c-3cea-3028-af20-026c846a11c6 | -12.5289 | -50.8427 | 2026-09-17 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 177.4 |
| fe66ee11-1cf2-3ffb-b973-3a0b06eff067 | -9.8517 | -46.9269 | 2026-09-17 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0b80a7e5-24bc-3fa1-a38c-6598b7bb9b5f | -11.8069 | -58.1759 | 2026-09-17 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| f596663c-b23d-360a-9444-168df2a5f593 | -7.3669 | -38.9584 | 2026-09-17 13:10:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 9799509a-d8bc-3c72-9595-fb11bc830874 | -7.0164 | -44.6413 | 2026-09-17 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 185.9 |
| fb3a5e45-eea9-3436-9aef-1ec097b457eb | -14.1937 | -45.1372 | 2026-09-17 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 15c7d74d-82ee-39a5-8b45-0eecb868b5ee | -10.7999 | -50.8455 | 2026-09-17 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 85f548d7-bfa8-31eb-8c4f-9692511676e1 | -10.8189 | -50.8436 | 2026-09-17 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 2950c484-2cf6-3064-9b7f-d5e4c0d0db91 | -10.8308 | -46.1569 | 2026-09-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| fb8d64f2-d2f8-321d-9b8e-1d81b817b73d | -7.7568 | -47.2927 | 2026-09-17 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 29a2d445-a95a-3bc3-a756-2b6378ef83a1 | -7.0084 | -43.6497 | 2026-09-17 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 189219a8-a76b-37fc-8da2-e65c5b6133d1 | -12.5097 | -50.845 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8c7f6aed-5fb2-35b3-a222-2c6d3889adde | -3.2028 | -53.9427 | 2026-09-17 13:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4c0676a5-c4f7-3cfe-b29a-616902c92e9e | -12.3568 | -50.8634 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 66a6cf40-736b-3db7-b1b5-d7cb839d96b8 | -7.8221 | -44.8632 | 2026-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 41f2a18a-35dc-36e0-a1ec-87232221f86c | -7.8033 | -44.8651 | 2026-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| fb4523bb-3486-37ff-8e44-063999f1e782 | -7.3669 | -38.9584 | 2026-09-17 13:20:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 9c15b353-c99e-3a75-9d28-a96910ce0904 | -9.734 | -45.8848 | 2026-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 232.4 |
| aab5c6a7-c245-3b4f-8b4b-11eccf084cb7 | -7.0349 | -44.6625 | 2026-09-17 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0552c0c4-76da-353f-b273-c3bd00d16ac4 | -7.3663 | -39.0091 | 2026-09-17 13:20:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 53dd25f2-52d2-32ad-beb1-ec400c35af39 | -12.5289 | -50.8427 | 2026-09-17 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 168ddd2a-2d9a-35e9-b380-26ddfe9c868a | -7.5664 | -42.6323 | 2026-09-17 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| dbb27fa7-12c0-3f64-83cb-4388402b14f4 | -7.0164 | -44.6413 | 2026-09-17 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 9dde697f-e62c-3b40-b76c-0b30e7d7ff6e | -13.6531 | -45.97 | 2026-09-17 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| f9973242-1fd5-38aa-b2e1-3e1f9c7a20ba | -11.8069 | -58.1759 | 2026-09-17 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 5fedb1ba-de20-3586-b913-6c9ebe0ca2ee | -7.6402 | -44.3303 | 2026-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 7eb0a810-480d-39f1-a49f-6838ec450c9f | -8.8644 | -45.8919 | 2026-09-17 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b97d6d1d-9f93-3c4f-8fa1-0d0163c4abd9 | -14.1547 | -45.1442 | 2026-09-17 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6eaa92b5-fa35-3ddc-8144-525f2c665ac3 | -12.7243 | -48.2734 | 2026-09-17 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 566181e3-9bbf-3a70-86d0-9f4b0055e6e4 | -11.3463 | -47.2585 | 2026-09-17 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4b8b4f61-6c35-356d-844d-e1e35202869a | -9.852 | -46.9046 | 2026-09-17 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 64c964e5-217a-396a-97ce-2cc895ae4cad | -12.7051 | -48.276 | 2026-09-17 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |


[Clique aqui para ver as próximas entradas](README89.md)
