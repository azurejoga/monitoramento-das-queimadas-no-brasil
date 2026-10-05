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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecba59b9-26b5-3c2d-9f81-b6ff45a204a1 | -8.54062 | -54.58189 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9a5181b2-178e-3a1b-b4c3-9613637d09b0 | -7.62019 | -45.30609 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2a28e4ea-1ced-38e9-bd61-07cd5c8b560c | -3.22401 | -54.30592 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 37861d0f-ac3e-3638-8629-46dab0ea622a | -8.5244 | -54.59525 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3fb87ae-1ffd-3285-b513-77e65ffa8c8f | -4.89498 | -43.46653 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32137835-6a55-34e9-8569-3f51c444ad60 | -2.48643 | -49.40654 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dee366f3-e1be-3d44-94b2-4cb4ecd7ed5d | -7.90151 | -44.19086 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3198cb4-c38f-317e-8f3a-3dff0dcbf584 | -3.0577 | -54.16918 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b04a2638-f4da-386d-a3f5-0d78ed248fa7 | -3.824 | -55.61082 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f2b6fe1f-b10e-3897-83ae-113973c1cb21 | -8.66067 | -54.57082 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f09c0727-7779-3ec0-af7f-bb8bfe6a8ee8 | -4.07942 | -59.1255 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 90f39da2-0ae3-3b16-a74f-8a3c62d2e7b9 | -6.93186 | -43.67939 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f8b87d96-4978-3473-969f-960eb1587840 | -8.59652 | -66.80778 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| cb240b3e-0145-3155-93ab-d5460dd43fec | -5.95002 | -41.3518 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| afcf1eff-7e08-38fd-9073-dac2c1e8033b | -3.11782 | -53.70286 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1b02b9e1-02df-3f14-a072-e72ffcff312f | -2.99546 | -54.11573 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb8ef88c-bfbd-3c3a-8c63-4bb9573a74c6 | -3.50795 | -54.6145 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 614db73f-38d3-3ac7-960f-ccafa3224301 | -4.3796 | -43.92382 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 457c6564-fee0-3042-855c-24bf3bcc9609 | -4.37942 | -55.16096 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| dbfc7911-033e-3104-b96f-b2039de77cbd | -3.0534 | -54.20582 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 952d4167-f775-32b4-a4fb-2c1da6f1e8ea | -5.50629 | -42.80586 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6fbaed36-9a78-38ea-abe4-72aeed2edfd6 | -6.6803 | -55.10425 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08d17a09-846d-3a3f-969b-2b52978db04c | -3.27325 | -54.00837 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a8919a6-88b3-3127-a1e9-7459e676aa6d | -6.92468 | -44.56023 | 2026-10-05 17:15:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66daf109-20b5-32fb-bfdd-2f7936a178aa | -6.61724 | -41.76737 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e7bf4d8d-c9ae-3079-86a8-ffcdd0dfb973 | -8.52923 | -54.5985 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 743184f1-0f67-3b67-bfb4-7919b947adcc | -4.02745 | -55.50291 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3dcf1042-2eea-301e-b00e-3f9b7fce1c50 | -5.68285 | -53.49472 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 81da0c7b-3585-3990-b6b6-84cd4e899f78 | -7.64944 | -44.37291 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b7e14fb7-44ff-3e21-92b3-537f2ef58237 | -9.29574 | -65.64583 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 7cf94922-32ef-3b17-a7e4-da0bd00c5f4d | -4.46023 | -54.96073 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b7247d59-599c-3035-bd75-a8c2017620cd | -2.85394 | -51.29468 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bdd7b712-8817-3e43-9ec4-d96fcab974aa | -2.99465 | -51.00677 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 237.4 |
| fa0fd4ac-3b27-3049-9718-8a6c1386115e | -3.29587 | -53.84567 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ececb56f-8a47-3998-bc7d-e0732b372976 | -8.52815 | -54.59122 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f29d4fe8-c229-3999-b3e5-d155d7314e6b | -4.86596 | -43.46361 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 595ccb60-8583-330a-9009-d3539a8f48af | -2.22873 | -44.79383 | 2026-10-05 17:15:00 | NPP-375 | GUIMARÃES | MARANHÃO | Brasil | 2104909 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ede727c1-1d1f-3a18-897c-aa3a7ab54c46 | -9.03155 | -45.16367 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3c7fef18-ad23-3a4f-a4ef-4b0884b6be75 | -3.67595 | -55.94898 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0b95b33f-bdbe-3e12-90e5-a47e765d15e1 | -8.04545 | -46.83236 | 2026-10-05 17:15:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67005f07-12a4-3697-8108-7d8f7519345c | -8.52778 | -54.59474 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bed14db8-58e4-360f-aa20-da190830b721 | -4.38278 | -55.16047 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 839ff4b9-724c-30ef-8d13-f68636a7999e | -2.67752 | -49.03459 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4288a17a-08f5-3fac-a0bd-bc68b5f1020a | -3.91701 | -44.14212 | 2026-10-05 17:15:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b3ba425-1236-3bfa-a79f-695f3e374978 | -8.59853 | -67.13219 | 2026-10-05 17:15:00 | NPP-375 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 84990ef9-de35-34ba-bb06-87fa9550fb99 | -3.50689 | -54.60759 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f365f09-f6d2-3cf4-a143-d1a66fccc426 | -6.4978 | -44.16713 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4d02225-6688-3685-8168-494f4330325a | -6.20928 | -44.805 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bb1f1e44-75ef-32a1-bc63-977d1f8e4b6e | -9.40235 | -65.88843 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c3f6cf6f-2453-38e0-8e04-59b94a1ffa78 | -3.28258 | -54.17995 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 53c004bf-5e07-3f9f-ac64-4ef53c055c6c | -3.19336 | -54.10586 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fc91c8fe-f98a-355d-834c-dd4123723e37 | -3.47573 | -55.42764 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 773701dc-2031-335b-bd35-04e805af8ec6 | -9.14852 | -65.55007 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 124f3721-ae34-3fbc-ac34-6d406a4d7f74 | -3.3762 | -54.10839 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 37cec53c-1533-3f2a-99a8-c84993759c42 | -10.30259 | -63.40303 | 2026-10-05 17:15:00 | NPP-375 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d705c45d-134a-3935-b667-8ef53ff3abe2 | -3.62668 | -55.28129 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 83996815-afa0-38cd-a44f-bc9775a2b8d6 | -3.11169 | -53.70736 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 264918a7-fed5-30aa-bd8b-ab140e9e83e3 | -6.90136 | -43.66945 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7e171b04-b455-3511-afee-0fd4b249eb5b | -3.06222 | -54.15437 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 87616e97-df98-3434-a3e1-91bea6835b03 | -9.10532 | -64.37319 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c5bb3316-22b0-38ab-aea8-f8ab756c2bf8 | -4.93817 | -42.71339 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 72360308-f10f-3d38-8eef-67ce7ee30fff | -7.21964 | -55.19445 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98d00eca-02f6-3867-a56f-00c4ff8f2498 | -9.82523 | -65.01834 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ccc89464-c552-33cb-9c00-e36a0619a365 | -3.2259 | -53.87465 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1c9d70f4-e609-3c36-bdf8-783ccc77618a | -3.10224 | -53.71235 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 04bc65f3-04f4-397e-b4da-0575831edd86 | -8.59694 | -48.07095 | 2026-10-05 17:15:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e5d47fa7-cab6-3110-9435-1c4d473d97f4 | -3.60368 | -54.04752 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c8fee280-58a3-3c3a-a0c4-550c6f4eda6f | -8.81714 | -49.31194 | 2026-10-05 17:15:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e031cb1-ec97-3ca1-8552-60b30508ea65 | -4.38028 | -43.92777 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4f0bfe1a-6f52-30b2-b5d3-ed55b8b048bd | -4.02436 | -44.82239 | 2026-10-05 17:15:00 | NPP-375 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 203c4af7-526c-3a1c-9d66-85f0f18984b6 | -5.55208 | -44.08854 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9245f2f7-8afb-32db-92f2-05be94a15130 | -6.31033 | -55.59364 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04ccb106-52f1-33d4-9724-1e6b79115663 | -5.85114 | -53.81911 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e4120a3f-e9fa-3cca-96e5-1d957465ff1c | -4.84853 | -42.19775 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9f6b8453-b3c2-3ba0-bfed-d0635d32cee6 | -3.05046 | -54.23097 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45448f4b-a404-38b6-8671-6f375970d850 | -4.13774 | -44.99387 | 2026-10-05 17:15:00 | NPP-375 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 34c3deb7-4c24-3686-b9c0-68298b9f9bd4 | -2.9944 | -54.10883 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 46bf062e-c63f-389f-930b-0fb974ba9aa8 | -2.98435 | -54.04327 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| cc8d3e40-a922-390d-a1ad-f854aeed71b7 | -7.21099 | -55.20318 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8efe4f65-e376-3809-8e37-0ff5f465cb72 | -8.65404 | -54.54947 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 75671b27-cca5-33c5-9261-12ae5be080cc | -6.72231 | -43.99695 | 2026-10-05 17:15:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 346db71b-10a5-3be9-b191-d6c506911eea | -4.80873 | -42.15696 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 72c0d160-da5d-3782-bb75-3ccee901d42a | -6.52139 | -55.39454 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f9a49a6-3a8f-310b-a27c-53968c1dc06c | -3.91764 | -44.14594 | 2026-10-05 17:15:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 963ae923-07e1-300b-9020-723495ef9855 | -6.51796 | -55.39505 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e50371e5-905b-3e43-b47f-b7971186e894 | -3.23923 | -53.87554 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b734aca2-8d07-3181-9fcd-470a27160465 | -6.72003 | -44.27498 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ac3b0786-26fb-3b0f-b7e6-351062d7ef67 | -5.34755 | -45.16498 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d34dba5a-f59b-3c9c-ba63-18e40687b22e | -3.67881 | -55.94481 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 2271bf9a-23a5-3a55-a7e6-7b61c99a0c59 | -8.86516 | -66.78976 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c959c903-ab4d-312a-b912-88afae8bf610 | -9.07031 | -66.09687 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cf61e71c-aa24-3530-a1b0-9151f69f9df1 | -3.51512 | -54.61695 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ee22b35-af13-362e-8e5e-4b6e48dbe182 | -8.77726 | -47.56053 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 65482f79-3322-38ea-b00e-f1a55d7108ed | -3.58291 | -55.40004 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef35c709-2401-30f0-a38b-6bf3c526bd8c | -8.65742 | -54.54897 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| def4165f-9f86-3109-b047-08b731a93c35 | -3.04609 | -54.22458 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f837148d-fd47-3a58-97cd-ad097b34d212 | -3.23365 | -53.88348 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 7ef2d3a9-27a6-3a1c-8d69-412f2822aef9 | -9.12406 | -64.38705 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a14c50e4-0c18-3872-821c-6bfd369e7c99 | -3.19177 | -54.0955 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3a173b4d-7034-31d5-b4eb-09c2cea45f24 | -4.44845 | -54.97325 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |


[Clique aqui para ver as próximas entradas](README116.md)
