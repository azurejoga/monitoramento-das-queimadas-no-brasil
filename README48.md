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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b37f4c73-0072-3bc6-95e0-282c4851c15a | -3.6049 | -54.5736 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d078aebc-3846-3774-ade9-a8b251f59d8d | -3.5861 | -54.6741 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| aa30114d-2b22-306e-b34d-ce8507e407a5 | -3.1114 | -53.8041 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a0d540d6-a755-36f5-a68a-31da0d9a4101 | -3.0917 | -54.1666 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 20bafa34-955b-3f0e-bea9-f5546cae9894 | -16.8642 | -40.5709 | 2026-10-08 01:50:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 20e20798-e972-3964-808f-c53620c5577a | -4.4506 | -47.9329 | 2026-10-08 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 478fbb4d-8f1c-33f7-938d-19b84b207018 | -10.434 | -47.2601 | 2026-10-08 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 96968fd3-0b76-3b9a-8264-62647018afb5 | -8.7231 | -45.1583 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 269.8 |
| 1bca62c2-e448-3699-add8-4ce44dc3a7c5 | -3.1601 | -50.6021 | 2026-10-08 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 77b296b1-52af-3504-8404-a192c3eec409 | -8.7423 | -45.1334 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ea5c7a6b-8f5d-3ca0-83b8-9982af219022 | -3.5332 | -59.4811 | 2026-10-08 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 7c3228f6-6d29-39ae-8add-02e5efd7215d | -5.7117 | -53.4862 | 2026-10-08 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| f288b253-5661-38f2-9ee3-52bce354844b | -3.0373 | -53.9469 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7bf729a0-0c0c-37df-80c6-094b7b4ad4c3 | -3.5516 | -59.4616 | 2026-10-08 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| d70a758c-1a3f-35a1-b783-4463b0ca3423 | -5.7376 | -45.1533 | 2026-10-08 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 332b6732-c943-34f8-96ad-22f21586a13f | -3.1697 | -58.6437 | 2026-10-08 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| b8572118-ec27-36ed-90e9-8e1aa99b86e0 | -3.5515 | -59.4807 | 2026-10-08 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 44e05e19-4f60-32a1-bd19-7dfd60def1c4 | -8.742 | -45.1563 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 6618faad-be6c-3850-9d4c-295317074340 | -2.8575 | -59.1107 | 2026-10-08 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| e0f6a24f-5847-3e2b-8616-c7496a7aa4ba | -5.6931 | -53.5073 | 2026-10-08 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 86b5d25b-baf6-31d5-a366-7f4dcec8a0e7 | -6.6317 | -43.73 | 2026-10-08 01:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 37b52c8f-3aa0-321d-a0bb-9e79eeaea89e | -9.4936 | -64.3518 | 2026-10-08 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| dbbdcd24-f017-3cb1-bdb7-9001010ed45c | -3.1879 | -58.6433 | 2026-10-08 01:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| bd0084e8-c89a-3277-b9e8-fcfb569065f6 | -9.4749 | -64.3713 | 2026-10-08 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ca0cc39a-0b23-31b9-b747-6954a9e0d46c | -2.4987 | -56.1659 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 90b95eba-7151-30eb-9a9b-1d8542c4acd7 | -3.073 | -54.2874 | 2026-10-08 01:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8405f6ce-ae9a-349e-a0cf-9616f969debd | -8.7225 | -45.204 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ab709af8-0c37-36e7-ae14-7b8ce8bf9bb8 | -5.9586 | -55.3648 | 2026-10-08 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| aac7802d-2564-3614-b77e-9a12b57bba39 | -9.1486 | -45.8158 | 2026-10-08 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 292dafee-ea42-3f9b-be6c-b6a872cba439 | -2.7152 | -57.472 | 2026-10-08 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 7a613c52-231c-3cb7-9bc4-48e3a27c25f9 | -9.0591 | -65.9396 | 2026-10-08 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3a86e279-2e32-30b0-b50e-0a13a516bd70 | -2.499 | -56.0675 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6fa653cf-7ceb-3a4d-a7c0-3e1fe7018bfc | -2.572 | -56.1842 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5a39628d-c380-3a02-9df7-23a3db93003f | -4.1176 | -59.8888 | 2026-10-08 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 51e3c1e6-cbdb-3291-8882-c9f6b270c4ca | -3.5493 | -54.6752 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d99fac24-0088-344a-80d9-8699671fa0c7 | -6.1431 | -47.9214 | 2026-10-08 01:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c1fd01dd-69d5-31ac-ab52-1688a0a17f69 | -7.0065 | -59.1223 | 2026-10-08 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8e5938d0-8256-3ec0-a76b-df872c0ce034 | -2.572 | -56.1646 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ef717ab0-3fb6-3770-9acd-46a01c2bdf2d | -4.4507 | -47.9112 | 2026-10-08 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c76a39c5-6f8d-3f51-aecf-32135c31819c | -3.8567 | -55.9769 | 2026-10-08 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| a8ca04f8-cf63-3374-97a8-49d549b58d9e | -3.8383 | -55.9774 | 2026-10-08 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 6bbac86a-3231-3e21-8ea3-857bd09723ab | -1.5306 | -54.5558 | 2026-10-08 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| bf37b73d-216c-3eb7-afa9-12dd1c7371bb | -2.517 | -56.1656 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| da3e0c5e-5433-3614-a391-8bc12413aa8d | -6.8952 | -43.6833 | 2026-10-08 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 95892f9e-5fd0-3350-ab16-8ddda61db8b7 | -3.1285 | -54.1657 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 6a160144-8a70-35a4-ab11-945d972ead91 | -4.3471 | -43.8021 | 2026-10-08 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 683e5913-1be2-371c-b996-f841467a985f | -9.4935 | -64.3706 | 2026-10-08 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 20ee2c3e-0529-3a4c-ae79-b99757cbb109 | -3.11 | -54.1862 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9d586fef-62d9-3b10-9cd2-79cbd6e2f612 | -9.475 | -64.3525 | 2026-10-08 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 79f1740e-9cc5-3d24-878d-35863cba69e1 | -3.5494 | -54.6552 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f13de5b7-1538-3ba6-9da2-cc7ee48e3f77 | -3.2499 | -46.9589 | 2026-10-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 68439036-e1ce-325b-8228-dee01d0a18fb | -8.7228 | -45.1812 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 226.6 |
| f3eeac6d-d8c9-36fb-9d4e-850721fcb892 | -2.4032 | -57.8848 | 2026-10-08 01:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2747ad83-3432-347c-9a16-55db458fc749 | -2.4805 | -56.1072 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 133a3f9d-2d57-3910-b712-06dea179c059 | -6.3163 | -43.3614 | 2026-10-08 01:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 3b88cece-3547-3c21-b222-f684642ece5b | -3.1101 | -54.1661 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 5596a5d6-b959-3603-b32d-f7811d44366c | -2.9448 | -54.1501 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 8e3f39db-ab3e-3341-a2c2-ba7cfddce56a | -16.8441 | -40.5761 | 2026-10-08 01:50:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 971ac416-1df6-3ec7-9484-2cd4dbae26ee | -3.1972 | -50.5592 | 2026-10-08 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| b238e632-7ddf-312f-b8ad-70f27c71934a | -2.7613 | -54.0941 | 2026-10-08 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8f75e3e6-9c75-3d1d-9ad2-2340ec719440 | -5.6932 | -53.487 | 2026-10-08 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 16d43f56-b13d-3c51-ad26-5af121bc471e | -2.3848 | -57.9044 | 2026-10-08 01:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 679e6612-bb07-38b0-a849-b2afa4dec1c6 | -3.0913 | -54.287 | 2026-10-08 01:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| edf60430-ae1d-34fe-81bb-c6042af6f9f9 | -10.4151 | -47.2623 | 2026-10-08 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 95d456ca-b12d-3fec-99a0-295783121156 | -5.7116 | -53.5065 | 2026-10-08 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 53d92786-77fe-3194-a96e-be5a18fe4887 | -3.586 | -54.6941 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| c5daef7c-352c-327d-b90f-b1c050fac24a | -3.531 | -54.6557 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7748c1a6-dc81-3043-a3c5-193fe6fba773 | -2.3849 | -57.885 | 2026-10-08 01:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5bc7d241-a721-3942-b64c-3a67f98a563d | -3.1102 | -54.146 | 2026-10-08 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ec776307-110c-3a87-842b-0a159a0df346 | -3.2157 | -50.5586 | 2026-10-08 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 50f1108b-e353-39e8-aa02-a45b1a9bb64b | -2.4805 | -56.1269 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 80e6d22c-b060-30d2-9dd5-f86bd02ad0fa | -2.4988 | -56.1266 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7ab98355-31db-3835-883c-e989c488ef56 | -17.1213 | -41.3421 | 2026-10-08 01:50:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| fdc59420-def3-39ba-a390-beb1b1b160ba | -2.4988 | -56.1462 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d8d25839-806b-3d5f-8621-cf947d71b04f | -3.0914 | -54.2669 | 2026-10-08 01:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 9f42e292-3ae9-337f-945b-33f7d14a87c0 | -10.4337 | -47.2824 | 2026-10-08 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 6475e9a0-e561-35af-b1ac-b35a34f046a5 | -6.9535 | -45.2619 | 2026-10-08 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3c7bf8f1-3899-3f8c-9d44-adcc3d9b785e | -3.0374 | -53.9268 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3b09c04c-8f48-3e2e-9657-bfba0fdbbc80 | -8.7039 | -45.1832 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| dde0c4dd-1460-3f0f-8f47-0331087cbae0 | -8.3882 | -46.3006 | 2026-10-08 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 70230407-3650-3819-8d8b-94e1bdf24a9a | -9.1294 | -45.8405 | 2026-10-08 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9ac04e7f-2328-3423-a3f8-642c34c5dcc4 | -6.1429 | -47.9432 | 2026-10-08 01:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4a085d6c-60c6-36d1-a455-4ca639ddd29a | -3.1115 | -53.7637 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f6dc1e6d-3a88-3a2b-ac2e-fdba9ae15d17 | -3.5865 | -54.5742 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| e5530347-c4f6-334d-b587-d4587874c4dd | -3.5698 | -59.4803 | 2026-10-08 01:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 3c65c833-3fec-3905-a2de-f7700ddd0b1f | -8.7417 | -45.1791 | 2026-10-08 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| ea9bce81-355b-33b6-899b-ea9842fb8f68 | -3.1114 | -53.7839 | 2026-10-08 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d54ca2cd-0342-3904-912e-9c516eb5c983 | -3.478 | -59.5779 | 2026-10-08 01:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| aba2d582-0bb4-343e-8c3f-2c117518b94d | -9.1483 | -45.8385 | 2026-10-08 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1c3d5684-bcff-3964-95df-76a89245d322 | -3.531 | -54.6757 | 2026-10-08 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| c101ed29-fe65-3ee1-8b6b-8c36375aada7 | -2.7796 | -54.0937 | 2026-10-08 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b8c3180e-2046-3cbe-87f3-c522984f1820 | -2.7797 | -54.0736 | 2026-10-08 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| fcfe451b-6ced-37d7-b36d-2cbf1e2c880a | -6.2342 | -52.8685 | 2026-10-08 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 97cdd00e-b415-3856-989c-a5fbc07a27e6 | -8.2184 | -46.3396 | 2026-10-08 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 5f0facf0-51b0-34bf-83a4-c2d3efa87156 | -2.4031 | -57.9041 | 2026-10-08 01:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d8ffad96-3a99-3f06-a46b-49161fd8dc69 | -2.5903 | -56.1642 | 2026-10-08 01:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e5aa3e60-674a-312c-850b-6c4497a99f26 | -8.537 | -66.9764 | 2026-10-08 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8db31bd0-add9-3602-8da6-7bc521cc0e6f | -5.7376 | -45.1533 | 2026-10-08 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1e87fece-e2ca-3bda-a117-70ae10f35175 | -10.4337 | -47.2824 | 2026-10-08 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 601da5e1-9a6c-3670-a60f-0a4b46f00175 | -6.8764 | -43.685 | 2026-10-08 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |


[Clique aqui para ver as próximas entradas](README49.md)
