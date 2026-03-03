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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c69f0681-c648-30fd-82a5-b345fb06ae4a | 1.12287 | -60.51769 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f52f793-1fa4-39a6-add3-c4abfac37f7e | 1.82847 | -60.85228 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db71ddbe-43da-30ff-af2b-e9284a88626a | 1.49148 | -59.90959 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9847bfd3-f54b-35bf-b7bd-9d169d418435 | 1.64751 | -61.05099 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92b7228a-e942-3c3a-ab2b-614374fb28ac | 0.31347 | -60.44 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9d7b080-029d-3592-ab10-7efc9f8912d9 | 1.78318 | -60.54173 | 2026-03-03 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81589b6c-4b52-347e-b7e7-24855d31e87c | 1.50397 | -59.91986 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db329dbc-d7b3-32b4-961a-11e30281605d | 0.93228 | -60.54006 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b1fe47f-a2d5-3e3a-926c-83d87caf778d | 1.11601 | -59.19735 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3538d6c-2d90-3db2-9baf-c5a1625f82f8 | 0.4975 | -60.50023 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0073e1f6-81ab-33ab-be27-ad3d78ec2d5d | 0.49684 | -60.49611 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92348012-d592-36ef-8b28-0e823d644ed3 | 0.77065 | -60.47857 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7090c91-6f4d-391a-a0e6-2f4bca59f9da | 1.50689 | -59.91525 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e67e3441-2825-3bea-bea1-58bb01658832 | 1.49857 | -59.90844 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3227cd0-cff8-33cc-8be9-252276ed5454 | 0.5653 | -59.90913 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acea9726-a054-3993-bfbd-b10022b6e511 | 1.07549 | -59.25317 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c1fe13-54b2-3f7f-80f6-7ace9a3ee725 | 1.50875 | -59.92724 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b3d8e05-a6cc-343e-9891-4a936bbc7075 | 0.49713 | -60.51421 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b7395ad-3dc8-370a-bd9c-e50eaca2e0d4 | 0.8719 | -60.46407 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7f99304-1ffe-303b-9b7e-97e84e51c5f3 | 1.4998 | -59.91644 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1403185b-85e4-3785-8329-017c728846e5 | 1.49918 | -59.91244 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6617c085-3c36-36ec-8008-f05d1a5cbe36 | -0.15677 | -60.74845 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ebbcf0-0e44-3957-89be-e5d6b9c4729a | 1.49271 | -59.91759 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31484c41-6da5-3484-af52-9f12f3973708 | 1.06517 | -59.25479 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d6abae-4dad-3862-a532-8ccbd22b0789 | 1.4921 | -59.9136 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 992f6acb-60d7-33fb-9d05-8bebebda3080 | 1.50813 | -59.92326 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1214ec2-dd86-3ff9-aaa9-aed371969447 | 0.96143 | -60.53264 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12e262f2-708e-38af-b5c4-477dcaff4df8 | 0.45461 | -60.39344 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52bc9c1-f4cb-3d5e-9ca6-aaebd3cc4fea | 1.51585 | -59.92616 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 953bd535-ebd3-3300-bd21-ef0353ff8454 | 1.47666 | -59.92704 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adbf97d9-3777-3405-998a-d553f88e5a6f | 0.49588 | -60.5132 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c7b0fa8-4c1a-326c-a977-32616b147220 | 1.5123 | -59.92671 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9e6556-e4da-3d64-a472-0709e944088c | 1.49023 | -59.92092 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 903fada6-f18c-32f7-8542-ae4d029da8be | 1.45541 | -60.06967 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14868dda-465a-33d9-a1cf-0784542aff15 | 1.50937 | -59.93126 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16de7ef9-c9fa-347f-b23b-a70e3b06392a | 1.50706 | -59.93983 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0290e51a-c8fc-3e7c-8ae0-31289521a0f9 | 1.49626 | -59.91702 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2b506ff-feae-38e6-aabc-636009ae9fed | 1.35818 | -60.06761 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f597c19-6a92-3310-9e97-23acf23e418f | 1.35755 | -60.06358 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4dcd3be-bec4-369b-87aa-9419488abcd3 | 1.50273 | -59.91186 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d43ee125-e7dc-323b-8f4b-a6ba249ed701 | 0.05524 | -60.98299 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd9adb0b-b37a-31e9-9a6e-a395772873a2 | 1.82777 | -60.84783 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44f05a53-978a-3734-a7e6-ea6176b4298d | 1.5146 | -59.91807 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027b57d0-b7b1-3b03-aecb-b9c8cb15de0e | 0.49521 | -60.50178 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70817f15-1623-3811-a73c-558e248d6f0f | -1.51349 | -54.52493 | 2026-03-03 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 943b013d-358d-37ad-961d-a608aa488af3 | 0.96441 | -60.52788 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25effedd-f9bd-3d99-b49a-ce698bdb7369 | 0.09259 | -60.62355 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab061504-68cb-3680-a42a-d964c46a39ff | 0.92302 | -60.52873 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 364fbb4a-29c7-3283-a065-14d07628900b | 1.6502 | -60.23922 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bc53b7a-2ef1-3b52-b14a-08709982eb06 | 1.51062 | -59.9393 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b7515f-c917-3dc6-8199-0f2ec70438c8 | 1.33614 | -60.0669 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13aa0c5c-5feb-3a5d-899f-1bdabecca545 | 1.54972 | -60.28728 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 697a1dd6-69c8-32a0-aadd-b2b1feadc753 | 0.31039 | -60.49085 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c1e768-8668-39b3-89a8-d070292d50bb | 1.48542 | -59.91355 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c74a234-848c-3ba1-94fa-26a89cb17f95 | 0.49585 | -60.50591 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efa31a68-e419-30e3-97b2-033be791e868 | 1.86592 | -60.40331 | 2026-03-03 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a24ff7b8-8c51-3b4a-8f31-c096a3a08643 | 0.06097 | -60.99554 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f997a2a-3f5f-3ad8-acd7-81229242a113 | 0.93508 | -60.31606 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f3ea09-c15a-3941-b7b3-e13073229a81 | 0.56882 | -59.90859 | 2026-03-03 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311d2942-22d9-3541-a3c1-23b0d8be4249 | 1.51168 | -59.9227 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df99007d-c5a7-3695-a443-5fa308a8b30e | 1.36112 | -60.06304 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed257dec-2396-3e86-98cd-5a0163c8b87e | 0.06029 | -60.99115 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba7bfdf-7772-3728-878a-d0541dd43fc5 | 1.50335 | -59.91586 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b976cc-7389-327a-9ce7-cb9b7292d172 | 0.08536 | -60.62471 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0366e71-3345-30a3-8435-9a7c88465e8b | 0.45885 | -60.39697 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd7f2e9f-a1ed-3049-bb02-78cd4a6bb493 | 0.08897 | -60.62413 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ef094d-3231-38d3-a566-3cd94435245c | 1.71903 | -60.30065 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e828f3da-0ac5-3e1b-a4c1-b5faacc0c542 | 0.92352 | -60.43191 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb2954d-1b0e-34eb-a602-5433dd5388f2 | 1.48793 | -59.91016 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a45d56dc-0f9c-3484-b23d-3893f4172f73 | 1.11945 | -59.19681 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40328ca3-5c62-34de-82e2-7c3e59c3c989 | 0.08789 | -60.62306 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7b4c458-bcdc-340c-bcf1-8b2e5d95a4ff | 1.55333 | -60.28671 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db2b27e2-18f6-308a-9157-081c32f60961 | 1.64928 | -60.23786 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0931d46a-445b-329b-a8e6-e7c5ea5ac524 | 1.51355 | -59.93476 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71cbb2e6-f2f0-3f45-a4fc-5bf0e8d5d018 | 1.47312 | -59.92765 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5e9ab7f-8979-319d-aea8-ebb5f373091a | 0.93734 | -60.42548 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a59ab8-89cf-32c4-8a69-37063d080043 | 0.93233 | -60.53711 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d56d390-f14e-3550-a9ca-5041cbebd573 | 0.92416 | -60.43605 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e53af61-fa32-379b-a3a3-162dc5642ce8 | 1.50627 | -59.91126 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| fc91c370-e24f-399d-942b-03d583cdb786 | 0.49754 | -60.49296 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04eaddc7-2cf2-3848-9bd4-ac4644355acf | 1.11886 | -59.1931 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9fc765-7ced-3ae0-a1d8-91ed0a737f9e | 0.17868 | -59.42723 | 2026-03-03 05:22:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09709b2a-dd15-33df-9a21-a2763ebec400 | 1.07263 | -59.25743 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9733985-f0d7-3733-aed0-93a6e28b18b3 | 1.35628 | -60.05553 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a7b04e2-c8ac-328f-9e63-9d7b7524194b | 1.48683 | -59.92658 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f765ce-7de1-3c1c-bc88-6efa6711d8cd | 0.92235 | -60.52454 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f49c23-3a67-3950-b4ef-3e6324fd42df | -0.15314 | -60.74788 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42416392-6899-32f4-8955-eb68b0965d25 | 1.48731 | -59.9254 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d72d9feb-16e6-35bb-84e9-20bf207ed3c5 | 1.65381 | -60.23865 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c40c82-17ea-3623-ae67-96658aa7aa77 | 1.64994 | -60.24198 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c65160a8-af55-3be1-8b15-f2c6b94fa65f | 1.48832 | -59.90897 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2421b010-2112-3a95-974e-9758539dc57b | 1.11375 | -59.2053 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51114506-46ad-3655-8ccd-0549bf769600 | 1.49564 | -59.91302 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04cea4d1-22c6-3bc7-851a-48b92cfc804e | 0.05825 | -60.97815 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b611e70-dcff-364e-b52b-309b0fade679 | 1.20608 | -60.61905 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6833d7e-fb57-3222-94c5-559e6b3988eb | 1.65084 | -60.24335 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 808be105-b834-3318-b46f-0142beabcf90 | 1.55695 | -60.28615 | 2026-03-03 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0439c3e-7eea-3676-9288-9a8df996eab3 | 1.1166 | -59.20106 | 2026-03-03 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab0633bd-a27e-3956-bec2-2b77a8412f78 | 0.49457 | -60.49765 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2679582-7fe1-36ab-84b5-187951f49045 | 0.96078 | -60.52845 | 2026-03-03 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
