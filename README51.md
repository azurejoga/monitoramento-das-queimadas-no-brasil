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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27cfa001-5e0b-324b-8977-9b738d54fc8b | -8.7417 | -45.1791 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| af8dce9a-5b5f-315f-bfa5-44eaef9591bc | -10.434 | -47.2601 | 2026-10-08 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f4bb781d-3344-36c8-9afb-6dcc416fb3cf | -9.475 | -64.3525 | 2026-10-08 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f75050b5-3e56-329f-a9b2-c7c4db791104 | -3.5515 | -59.4807 | 2026-10-08 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| bd19c8dd-7934-301b-96a9-834c3e8244e2 | -6.6317 | -43.73 | 2026-10-08 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 259.1 |
| f1a0e23f-fbc4-3609-8651-1d1ba4e94f3a | -6.6315 | -43.7533 | 2026-10-08 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 133b4c77-6c2e-31f2-9f95-18947d45d655 | -8.7234 | -45.1355 | 2026-10-08 02:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ea97519b-7a65-317b-9ea6-610989ca4942 | -3.0373 | -53.9469 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 7e317da8-cfb8-3372-a319-a94ddca054b5 | -2.4988 | -56.1462 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f2770882-2cc3-3920-b33a-2401c5a459c9 | -3.0191 | -53.9071 | 2026-10-08 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| dffe67a1-bbbf-38d0-b210-458f162cdf99 | -6.1429 | -47.9432 | 2026-10-08 02:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0f30e781-756a-37a0-b242-56d2c0597843 | -2.7796 | -54.0937 | 2026-10-08 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3b5ca5bf-f95c-30e9-ae8c-805a3853b3d9 | -3.1697 | -58.6437 | 2026-10-08 02:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 6d5de708-45ad-3c39-82d4-4a230af1f678 | -3.8383 | -55.9774 | 2026-10-08 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e9b1581c-181b-362e-9aef-758906446e15 | -2.499 | -56.0675 | 2026-10-08 02:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0ede251a-5b17-3eae-80bc-5615de91ccb6 | -8.7234 | -45.1355 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 69ffb50f-18b6-3ed1-b3df-5fd246162232 | -3.478 | -59.5779 | 2026-10-08 02:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| e9e87d9d-47c2-33b9-9f3b-7e9b39f81352 | -3.1101 | -54.1661 | 2026-10-08 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| de5fd93e-f1b2-3251-b3cd-432cadf0e007 | -6.6505 | -43.7284 | 2026-10-08 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 6dd4c1a6-a2be-36f2-93f8-0e2a31a3800c | -8.7228 | -45.1812 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| f15b2423-f6af-39ef-8b6e-29a3ac3e267e | -6.6315 | -43.7533 | 2026-10-08 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| b500d9cb-8030-350e-8c15-3645da18ae47 | -6.15 | -39.4409 | 2026-10-08 02:30:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 00bfabcb-b4ee-3b32-a6ed-59ede40bc303 | -3.8383 | -55.9774 | 2026-10-08 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| d0b690fc-bf32-3d10-bb7b-28ffdecdfb63 | -10.434 | -47.2601 | 2026-10-08 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 101da1aa-3637-33a8-9df0-bdcd68877c38 | -2.4031 | -57.9041 | 2026-10-08 02:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a44ce367-d82c-3890-977e-d7239cf1ff7c | -2.4987 | -56.1659 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 13e96ede-5f0b-3982-9195-51bf6d3ffdbd | -6.1431 | -47.9214 | 2026-10-08 02:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 6cfb3f3a-09e3-30b5-b571-f5f98d89e8f4 | -3.0373 | -53.9469 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| f1f7128a-dd3a-3d6b-b274-de81eb622c97 | -3.1285 | -54.1657 | 2026-10-08 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 07d3c456-375c-3e98-933d-940bd13ad436 | -8.7562 | -67.693 | 2026-10-08 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 81e9146f-415f-3ed2-87f2-beb934a1f938 | -9.4749 | -64.3713 | 2026-10-08 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e06600fa-57e6-39cb-8185-10996683513f | -2.7796 | -54.0937 | 2026-10-08 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| db421ce1-2723-3198-be02-be012dfa1a5d | -2.572 | -56.1842 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| fb22fab8-046a-310e-ab8c-d38ddcdb4d66 | -9.475 | -64.3525 | 2026-10-08 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c001d146-99d8-35bb-931d-237481383116 | -6.6503 | -43.7516 | 2026-10-08 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 97d8212b-4d02-3f63-956b-e26a39fdaa81 | -10.4147 | -47.2846 | 2026-10-08 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7445ee30-44d8-3fbf-91fd-1cba153b8a2a | -10.4151 | -47.2623 | 2026-10-08 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e8ea28e1-0f6d-3f93-ae67-b5a2efbef127 | -2.8575 | -59.1107 | 2026-10-08 02:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 52b8a0a9-08e8-342e-b8dc-e4bb4831824c | -6.6129 | -43.7317 | 2026-10-08 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 67143f01-d586-3697-851a-14fd5fbf2167 | -2.4988 | -56.1266 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c1941bb2-08d5-3dcf-a36e-ec17d15b5514 | -3.1298 | -53.7834 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 09134eef-c8bd-3d93-8329-c1f1988db8f9 | -3.5515 | -59.4807 | 2026-10-08 02:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 31ab1668-40e7-3dd8-bd0a-7ab23794c4de | -2.572 | -56.1646 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6db6c50d-62e3-38e5-937c-b79d55f8c4ec | -4.3471 | -43.8021 | 2026-10-08 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 54d7a436-6472-3268-80ad-3eb5ac0c2f30 | -8.7231 | -45.1583 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 16e10f3b-4be5-36bc-8a46-8d5aaef3bc12 | -5.7116 | -53.5065 | 2026-10-08 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 511368a1-6e89-3ca9-b51a-02605ef0aafd | -2.7797 | -54.0736 | 2026-10-08 02:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eca5b15e-33f7-3d7f-9bf5-2e1072343d14 | -2.4805 | -56.1072 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3532d79e-b82d-3350-9601-09f76ee8e32c | -3.1115 | -53.7637 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| cfc154c9-5d4c-3844-826d-379302928808 | -6.1429 | -47.9432 | 2026-10-08 02:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 94653516-59d0-303b-acd1-8439c797246d | -3.6049 | -54.5736 | 2026-10-08 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| cc5a3c17-7bad-38c8-88b3-4f9358e9ce8b | -3.531 | -54.6557 | 2026-10-08 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 491e78b5-dd1e-3159-afb6-0afb7783802f | -4.4507 | -47.9112 | 2026-10-08 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9df2b2c2-dc2d-3a2f-8479-b982e280041a | -3.0741 | -53.946 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 02253d31-89f4-3a17-bcce-f2dfc08fae8a | -6.1617 | -47.9201 | 2026-10-08 02:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7c58b00e-fc82-33f6-959f-c49e922dcd43 | -2.4988 | -56.1462 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| cb398326-c0a5-3f36-8bc0-12b17d07c21c | -2.4805 | -56.1269 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c58e8b05-8e21-3995-970c-5cc8e5606f5f | -3.531 | -54.6757 | 2026-10-08 02:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 7133cac2-e85b-313e-a97c-7e6f6f23ee28 | -7.0065 | -59.1223 | 2026-10-08 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8cd08f42-b62e-3738-a5ad-c224dcc212d4 | -8.7561 | -67.7115 | 2026-10-08 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3d31412f-07f7-31de-a943-50ca649fe2cd | -3.0374 | -53.9268 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| d751ba99-9cda-3cd8-8bb0-0e9357eadd53 | -6.6317 | -43.73 | 2026-10-08 02:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 278.8 |
| e3e4a172-a9c7-35f1-9a69-b59299ea3feb | -3.11 | -54.1862 | 2026-10-08 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b3ee5101-3b64-3cfd-b0d0-043f152cf432 | -9.4936 | -64.3518 | 2026-10-08 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f84219bb-7fed-3c10-a5ff-af65cb72e79d | -3.0913 | -54.287 | 2026-10-08 02:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8be60887-5555-33a7-8d93-5e1d66b4872c | -3.8567 | -55.9769 | 2026-10-08 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| dc822606-0436-357e-85ca-e1025e57f355 | -2.517 | -56.1656 | 2026-10-08 02:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| fb148c6a-28b1-39a9-a4eb-6fde19d6f3e7 | -10.4337 | -47.2824 | 2026-10-08 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9b305c88-fd08-3db6-83de-3e0d8a0d07a9 | -5.7376 | -45.1533 | 2026-10-08 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bab5fa84-d612-3bbc-85be-68ad7bc9437a | -3.1114 | -53.7839 | 2026-10-08 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e43d92fd-2f0b-3a40-bd1f-823fa76b0da5 | -8.7423 | -45.1334 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 07dbbb1b-5fa6-3db5-9b44-a910c3fb37d2 | -5.7117 | -53.4862 | 2026-10-08 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ce82d7b5-3fa5-3a78-814d-e6745f682779 | -5.6932 | -53.487 | 2026-10-08 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 530b6754-0a96-3e2d-b2ee-82ebe115e691 | -8.742 | -45.1563 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 4f16627b-150c-369d-a80f-cd005f65da64 | -8.7417 | -45.1791 | 2026-10-08 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 105a843d-742e-35e9-bdaf-9e942e29bed9 | -3.1697 | -58.6437 | 2026-10-08 02:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| cbc60cef-ea4a-362c-910f-116372237266 | -5.7376 | -45.1533 | 2026-10-08 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 597e5d97-70a1-3f6b-9496-ef07362e9d97 | -6.6505 | -43.7284 | 2026-10-08 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ecb93e89-3cfc-3336-8c7f-06ba3db94894 | -6.6503 | -43.7516 | 2026-10-08 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9919973c-848a-3ec3-9b09-db4c0206cefb | -3.073 | -54.2874 | 2026-10-08 02:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 764986c7-40ef-3f83-849e-0efc7dc786b0 | -6.1429 | -47.9432 | 2026-10-08 02:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3a076654-b3ea-3073-afd8-69c3e36a3464 | -6.6129 | -43.7317 | 2026-10-08 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| cda868bb-af6d-380d-aed1-aebcd5b97206 | -2.4805 | -56.1269 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 426236da-6d4f-3b8c-b708-fc9ccf8ad44b | -2.4032 | -57.8848 | 2026-10-08 02:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 203f29f4-4fda-3f06-a1bd-2ff8f34af472 | -8.7417 | -45.1791 | 2026-10-08 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3f18658c-3b2c-3c92-8715-343028f621d4 | -6.6315 | -43.7533 | 2026-10-08 02:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 215.7 |
| ac164e5d-6bd0-3eaf-bef0-71583a8ba762 | -2.499 | -56.0675 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e28147fd-2da7-3ac1-bb41-ddd69c721957 | -2.4805 | -56.1072 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a137e779-e25c-3c11-9b4f-197f4ce8c7a9 | -5.6931 | -53.5073 | 2026-10-08 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4a481f96-5380-3bcb-a555-9a62c7caa88f | -8.7228 | -45.1812 | 2026-10-08 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.2 |
| d6fa87c4-0ceb-3b3a-9b05-dbeb6a4961ab | -3.1101 | -54.1661 | 2026-10-08 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 7348e7fd-702c-3360-b459-3a26474c08fd | -6.1689 | -39.4391 | 2026-10-08 02:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 0dac0e64-231c-33ce-b28f-32f92068f191 | -2.4987 | -56.1659 | 2026-10-08 02:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 6cb8b0a8-839d-3b43-b81b-ec4aa4bd9de8 | -3.5515 | -59.4807 | 2026-10-08 02:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| abb985eb-30ba-3249-89a9-245203c3415d | -8.7231 | -45.1583 | 2026-10-08 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 6a220c56-5ab9-398a-a6de-7975a3ca8acd | -9.475 | -64.3525 | 2026-10-08 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2af59a63-2173-3bdc-b24a-0c3299a3b01a | -9.4936 | -64.3518 | 2026-10-08 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 60ab8e3c-792d-3c33-aaf1-bfc3e8813213 | -3.1115 | -53.7637 | 2026-10-08 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 2c875cef-db92-3689-8652-84d039c2a471 | -8.742 | -45.1563 | 2026-10-08 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 263.6 |
| ce2fc532-4631-3c8a-9c7a-e32d72a544bb | -8.7423 | -45.1334 | 2026-10-08 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |


[Clique aqui para ver as próximas entradas](README52.md)
