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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f44cc7e8-7202-3e4e-bd85-45a1a95eec3d | 2.7267 | -60.3726 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 789.5 |
| 500dc926-fd35-3a12-b64f-dca12cbc8f58 | 2.7085 | -60.3729 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 447.6 |
| 543be69d-052a-3c15-bbed-5206cc0abffc | 2.7084 | -60.3919 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 173.5 |
| d2cc520a-fcc2-3bca-bdcc-a9867d9e23d7 | 2.7268 | -60.3536 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 243.3 |
| 32f24633-7544-3fbb-bf09-3b1e71ab6c2a | 2.7085 | -60.3539 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 61cd73a6-2de8-3455-9626-55982253b029 | 2.7267 | -60.3916 | 2026-03-10 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 264.1 |
| 2c0be132-b551-3a02-bd31-6884f0dadf73 | 2.7085 | -60.3729 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 317.1 |
| 36812452-1464-39c3-9435-d2596d43c567 | 1.7049 | -60.2901 | 2026-03-10 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 070cfc72-3dc5-3697-8aa8-55fa5c50d96e | 2.7267 | -60.3726 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 786.2 |
| f60b1555-7169-3196-95af-77c47f3de1c3 | -10.0651 | -36.29 | 2026-03-10 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 3d4aefa3-9ad5-3203-8a8b-664f26454578 | 2.7267 | -60.3916 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 294.5 |
| 4a54fe44-1811-30c2-b018-9f53c892554a | -10.0265 | -36.2969 | 2026-03-10 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 12f66faf-dfd0-31f3-ac66-259f19b65b3c | -10.0463 | -36.2664 | 2026-03-10 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| bed2c947-d119-3e6e-b8ac-7898cdd137bf | -10.0458 | -36.2935 | 2026-03-10 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 318.7 |
| d003da8d-d2c3-3e8d-9769-4dd6a771ee57 | 2.7268 | -60.3536 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 202.4 |
| c57eced2-42b6-35dd-89ce-c49900e932ca | 2.7085 | -60.3539 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e48713c8-fa3a-3611-b3c6-7648aacc7bf0 | -9.9879 | -36.3038 | 2026-03-10 00:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 7564ca37-7955-37ed-abab-adf909fe1594 | -10.0453 | -36.3205 | 2026-03-10 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 71aaf906-d832-36cd-ae1a-7fa9266cba32 | 2.7084 | -60.3919 | 2026-03-10 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 5132021b-da72-3fe0-a79b-af2f4119ac7f | 1.7049 | -60.2901 | 2026-03-10 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3a42fed7-c229-3366-8c94-380d17107577 | 1.7765 | -61.2548 | 2026-03-10 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 55d47757-6a26-3cbf-af50-8eed0e3feba9 | 2.7084 | -60.3919 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 104.1 |
| fbfe433b-bd03-361d-ad53-e1444eeaaeea | 2.7085 | -60.3539 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 20e2f353-c13d-3142-b4d4-bbcf610a57ef | 2.7268 | -60.3536 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 204.8 |
| c6817ad6-142d-32bc-95ef-58db682b85ef | 2.7267 | -60.3726 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 665.8 |
| 72165610-38fc-3b4d-a6a6-8a4d55f0af80 | 2.7267 | -60.3916 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 213.2 |
| 7a92831a-aaa4-3784-b13a-ebd6d6df2d43 | 2.7085 | -60.3729 | 2026-03-10 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 260.0 |
| 761d6943-730a-3043-8aec-beb8a80c9031 | -9.8018 | -35.9583 | 2026-03-10 00:50:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| b89c56ed-eaf3-388f-bca5-d1529da61d72 | -9.8013 | -35.9855 | 2026-03-10 00:50:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.6 |
| 9456782a-0fb2-3066-b113-6fceb744af7a | -10.1928 | -36.6699 | 2026-03-10 00:50:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 4c3da376-d6cd-3a60-af66-3d1e552f23fe | 2.69025 | -60.25293 | 2026-03-10 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f8fe0e5e-c398-36d9-849b-cd1c39866b2f | 2.90286 | -61.06246 | 2026-03-10 01:07:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c31db6e7-12dc-32ed-a584-c9585d5ede3e | 2.7207 | -60.37812 | 2026-03-10 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 3ce25732-aae8-3ce5-95ae-d0961c2fb991 | 2.6889 | -60.26289 | 2026-03-10 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 83d078e4-a021-3b5f-ac9c-340d99c58588 | 2.91319 | -61.05445 | 2026-03-10 01:07:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c994176c-3ec9-37a8-b767-f235c505f52d | 2.7114 | -60.37683 | 2026-03-10 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 98f3d79c-6b39-39fe-b583-dd353c4a2bf1 | 2.71935 | -60.38794 | 2026-03-10 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5d834c3a-945a-3d74-b1f0-970b80075781 | 2.73137 | -60.36957 | 2026-03-10 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e349772f-9f3c-3fb8-8cb7-96c1f7f4d31c | 2.72206 | -60.36828 | 2026-03-10 01:07:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 75b3a6a3-8618-3c52-907a-d6c130841a61 | 2.96044 | -60.04501 | 2026-03-10 01:07:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d61c1678-1ddb-3fe6-b085-5a46922a01f1 | -10.026 | -36.324 | 2026-03-10 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 152.7 |
| 2d97f8ad-7651-39a2-aa8f-91054fe92a1e | 2.7085 | -60.3729 | 2026-03-10 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4d4500b3-c360-3b83-8b52-285eab1736f2 | -10.0453 | -36.3205 | 2026-03-10 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 88.9 |
| a86d02db-dcc9-3597-99e7-d31fcedcd3bc | 2.7267 | -60.3726 | 2026-03-10 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dd4e749f-a10d-3284-939b-ea37dd39e9b8 | -10.0453 | -36.3205 | 2026-03-10 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 134.3 |
| adc2ccde-144f-330f-a157-bb05913a1408 | -10.0484 | -36.1581 | 2026-03-10 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 136.6 |
| ef2703a7-3e6d-390d-80ed-86420af8f644 | 2.7085 | -60.3729 | 2026-03-10 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1b8a840d-d766-32c3-a8c2-166839c77aba | -10.0677 | -36.1546 | 2026-03-10 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 128.7 |
| fa105d96-5ab5-3f83-80a7-0ad11313aa9e | -10.0478 | -36.1852 | 2026-03-10 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 220.6 |
| 7b8db664-47ca-31a1-a1a0-f7a878e14c90 | -10.026 | -36.324 | 2026-03-10 01:30:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 135.4 |
| 726866aa-8aaf-39ec-baec-a29d4b28f918 | 2.7268 | -60.3536 | 2026-03-10 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 29ce28b3-4be3-383a-b5c2-2e3e54d0a623 | 2.7267 | -60.3916 | 2026-03-10 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 86cd7ef8-25d6-34f7-893d-3c824f064a6c | -10.0672 | -36.1817 | 2026-03-10 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 203.9 |
| 9994104b-0447-3369-809b-e41090c73526 | 2.7267 | -60.3726 | 2026-03-10 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 6fd3484e-fb34-3845-83c3-951574a171a6 | 2.7084 | -60.3919 | 2026-03-10 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 82cf820c-b17d-3d61-aa85-4f8db325eb37 | 2.7267 | -60.3726 | 2026-03-10 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 626b3001-d19d-3204-a51f-07f76898a88a | 2.7085 | -60.3729 | 2026-03-10 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bc3df931-6b66-3c90-b7c1-e220e15b579f | 2.7267 | -60.3726 | 2026-03-10 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a8c56c8f-52f8-33f0-924a-278da0a5da16 | -9.7221 | -36.1077 | 2026-03-10 02:30:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| f0f48278-4594-385b-b84a-2f8a74d56c2d | -9.7221 | -36.1077 | 2026-03-10 02:40:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| a704cb12-9d5a-38d5-a716-93e6f4ee87cd | -10.178 | -36.4313 | 2026-03-10 02:50:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 8758cafe-2cc8-3697-9ab0-e53545715703 | -10.1775 | -36.4582 | 2026-03-10 02:50:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 2bfb1e38-565a-392f-8101-8d62e2fb7369 | -10.1968 | -36.4547 | 2026-03-10 02:50:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 46d63030-ef5b-335b-a341-da92aef24ee5 | -10.1775 | -36.4582 | 2026-03-10 03:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 2b545f11-9864-392b-982e-c512f152ff66 | 2.7267 | -60.3726 | 2026-03-10 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 326f4d4c-b51f-3520-b305-f3c3a26c76ba | -10.178 | -36.4313 | 2026-03-10 03:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| ec9ddb19-d566-3732-8b38-a445edbe2821 | 2.7085 | -60.3729 | 2026-03-10 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ab6d12a4-3732-3a92-8a0c-8d6ea2866e88 | -10.201 | -36.2386 | 2026-03-10 03:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| e57d5422-ef26-3f19-bf1a-b20f4f89341a | 2.7267 | -60.3726 | 2026-03-10 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8c8dab18-6e6c-3903-b2f6-c91fcb4abefc | -11.5593 | -38.26508 | 2026-03-10 03:10:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 43872d27-87f7-3acc-803c-142a158808e1 | -11.55321 | -38.26384 | 2026-03-10 03:10:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4dd6a842-f43b-304e-8d10-e7b779b26f17 | -10.19798 | -36.24393 | 2026-03-10 03:13:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8f00ada7-e609-3e1e-8739-cb6e668eb299 | -10.19867 | -36.24033 | 2026-03-10 03:13:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 577b5eef-b267-3575-80f8-61afd69cce1e | -10.18287 | -36.44287 | 2026-03-10 03:13:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4e85eeb2-3111-323a-b561-78e28bd5c538 | -10.1814 | -36.45058 | 2026-03-10 03:13:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8581e6d4-aeca-3bb2-8509-f79920a8a243 | -10.18696 | -36.45171 | 2026-03-10 03:13:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| bc0b259a-f6c6-3d96-a614-973476297f8c | -15.72781 | -41.4385 | 2026-03-10 03:13:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| efff2e00-ced9-3923-97dd-67fca0a4520d | -10.18214 | -36.44674 | 2026-03-10 03:13:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 8.1 |
| bdf9b632-dcff-3e5b-b650-86ba7cf5a347 | -15.72634 | -41.44505 | 2026-03-10 03:13:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc321bdf-5679-30c5-b003-3d314a242285 | -10.19729 | -36.24755 | 2026-03-10 03:13:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 4df361ae-b4ec-3d61-93e9-b2edf525dc2d | -10.18771 | -36.44776 | 2026-03-10 03:13:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c51caa35-dd35-3ef6-9bdf-3f2abaa79b21 | -10.19249 | -36.24284 | 2026-03-10 03:13:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ef005702-b3a0-3f74-ba5b-65a30967fa70 | -9.81793 | -36.12726 | 2026-03-10 03:13:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d46446e4-e813-3890-934c-c7e891a8fc50 | -9.81861 | -36.12365 | 2026-03-10 03:13:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 25cbe24d-2f5f-36e5-bfe6-5674f2fd6da9 | 2.7267 | -60.3726 | 2026-03-10 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 2b00cc44-f317-37ae-9dc8-64699a8b90de | 2.7267 | -60.3726 | 2026-03-10 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8cb3ba8f-93a6-3f7c-a7a8-bb3850c0c50c | -9.81938 | -36.12415 | 2026-03-10 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9711d2aa-1159-3d78-b69b-bedebe6b1230 | -10.20016 | -36.24212 | 2026-03-10 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ee400430-c21d-351a-ab96-f22baa28dc69 | -11.57724 | -38.2457 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d87fbbee-797f-325b-908f-3d071a03447e | -11.55723 | -38.26645 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aacca0e2-96f4-37f5-abec-2a053f935ff8 | -5.05178 | -37.41446 | 2026-03-10 03:32:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d99314b-9cd1-3c25-89da-bdc1734bdda1 | -9.93158 | -39.22287 | 2026-03-10 03:32:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27b47b26-a8f0-3633-87ca-c3db4d9a6620 | -11.58121 | -38.24639 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afb7461c-c5ae-3275-8a77-501c76828dfa | -11.56656 | -38.25998 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a374ebea-4bbf-3ad8-bf7a-29df4f892d78 | -9.57395 | -40.59668 | 2026-03-10 03:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50697463-57de-3340-ba4f-ffbfbe0c1d82 | -10.23993 | -37.43336 | 2026-03-10 03:32:00 | NOAA-20 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47fadbdd-b382-3314-9268-b30dc8b9fa54 | -11.55785 | -38.26294 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c49696a5-4071-33e1-9049-ca4a158b9176 | -9.81577 | -36.12353 | 2026-03-10 03:32:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2e788cbb-e869-3960-af23-9b3263610a86 | -11.55326 | -38.26573 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd4d9567-1f88-37e4-bd88-24dc7d81ad99 | -11.56182 | -38.26365 | 2026-03-10 03:32:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
